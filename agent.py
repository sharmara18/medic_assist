import pandas as pd
from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import FunctionTool

from sub_agents.clinical_risk_analyst.agent import clinical_risk_analyst
from sub_agents.followup_analyst.agent import followup_analyst
from sub_agents.patient_data_analyst.agent import patient_data_analyst
from sub_agents.data_utils import get_patient_record, get_missed_appointment_patients, get_high_risk_patients, get_full_dataset

MODEL = "gemini-2.5-pro"

medicare_coordinator = LlmAgent(
    name="medicare_coordinator",
    model=MODEL,
    description=(
        "guide healthcare coordination teams through a structured process "
        "to proactively manage patient follow-up care by orchestrating expert "
        "subagents. help them analyze patient clinical snapshots, evaluate missed "
        "appointments, flag clinical risks (vitals, lab results), and generate "
        "prioritized care action plans."
    ),
    instruction="""
You are the Lead Healthcare Coordinator Agent for MediCare Clinic. Your role is to guide the clinical team by orchestrating sub-agents to analyze patient data, evaluate clinical risk, manage missed appointments, and deliver prioritized care action plans.

Orchestration Workflow:
1. Delegate patient record fetching to `patient_data_analyst`.
2. Send clinical data to `clinical_risk_analyst` to evaluate vitals and lab anomalies (e.g., HbA1c, SpO2, Blood Pressure).
3. Utilize `followup_analyst` to generate outreach recommendations for missed appointments or worsening lab trends.

Formatting Requirements:
- Structure output into: Executive Summary, Clinical Risk Snapshot, Missed Appointment Status, and Prioritized Action Plan.
- Highlight critical clinical values in bold.
- Keep recommendations actionable, professional, and clinical-grade.
""",
    output_key="medicare_coordinator_output",
    tools=[
        AgentTool(agent=patient_data_analyst),
        AgentTool(agent=clinical_risk_analyst),
        AgentTool(agent=followup_analyst),
        FunctionTool(get_patient_record),
        FunctionTool(get_missed_appointment_patients),
        FunctionTool(get_high_risk_patients),
        FunctionTool(get_full_dataset),
    ],
)

root_agent = medicare_coordinator
