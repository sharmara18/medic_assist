from google.adk import Agent
from google.adk.tools import google_search, FunctionTool
from ..data_utils import get_patient_record, get_full_dataset

MODEL = "gemini-2.5-pro"

patient_data_analyst = Agent(
    model=MODEL,
    name="patient_data_analyst",
    instruction="Given a patient ID or dataset query, retrieve and summarize patient data accurately.",
    output_key="patient_data_analyst_output",
    tools=[FunctionTool(get_patient_record),
    # FunctionTool(get_full_dataset)
    ],
)