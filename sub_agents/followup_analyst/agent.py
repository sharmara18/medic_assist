from google.adk import Agent
from google.adk.tools import google_search, FunctionTool
from ..data_utils import get_missed_appointment_patients, get_high_risk_patients

MODEL = "gemini-2.5-pro"

followup_analyst = Agent(
    model=MODEL,
    name="followup_analyst",
    instruction="Formulate prioritized outreach recommendations and follow-up care actions for high-risk patients or those who missed appointments.",
    output_key="followup_analyst_output",
    tools=[FunctionTool(get_missed_appointment_patients), FunctionTool(get_high_risk_patients)],
)