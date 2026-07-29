from google.adk import Agent
from google.adk.tools import google_search, FunctionTool
from ..data_utils import get_high_risk_patients, get_patient_record

MODEL = "gemini-2.5-pro"

clinical_risk_analyst = Agent(
    model=MODEL,
    name="clinical_risk_analyst",
    instruction="Analyze vital signs, lab values (e.g., HbA1c, BNP, BP, SpO2), and medical notes to flag severe/moderate clinical risk factors.",
    output_key="clinical_risk_analyst_output",
    tools=[google_search,
    # FunctionTool(get_high_risk_patients), FunctionTool(get_patient_record)
    ],
)