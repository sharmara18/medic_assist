import pandas as pd
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

# --- 1. Load Data ---
DATA_FILE = "patient_data.xlsx"
df_patients = pd.read_excel(DATA_FILE)

# --- 2. Define Tools for the Agent ---
def get_patient_record(patient_id: str) -> str:
    """Fetch clinical snapshot and details for a specific patient ID."""
    record = df_patients[df_patients['patient_id'].str.upper() == patient_id.upper()]
    if record.empty:
        return f"Patient ID {patient_id} not found."
    return record.to_json(orient="records")

def get_missed_appointment_patients() -> str:
    """Fetch list of patients who missed their last scheduled appointment."""
    missed = df_patients[df_patients['missed_last_appointment'].str.lower() == 'yes']
    return missed[['patient_id', 'patient_name', 'diagnosis', 'days_since_last_visit', 'notes']].to_json(orient="records")

def get_high_risk_patients() -> str:
    """Fetch patients with abnormal vitals or lab values (e.g. Systolic BP > 140, SpO2 < 92, HbA1c > 9.0)."""
    high_risk = df_patients[
        (df_patients['vitals_bp_systolic'] > 140) |
        (df_patients['vitals_spo2'] < 92) |
        (df_patients['missed_last_appointment'].str.lower() == 'yes')
    ]
    return high_risk[['patient_id', 'patient_name', 'diagnosis', 'lab_test', 'lab_value', 'vitals_bp_systolic', 'vitals_spo2']].to_json(orient="records")

# --- 3. Define Sub-Agents ---
MODEL = "gemini-2.5-pro"

patient_data_analyst = LlmAgent(
    name="patient_data_analyst",
    model=MODEL,
    description="Extracts and summarizes clinical data, lab results, and vitals for a given patient.",
    instruction="Given a patient ID or dataset query, retrieve and summarize patient data accurately.",
    tools=[FunctionTool(get_patient_record)]
)

clinical_risk_analyst = LlmAgent(
    name="clinical_risk_analyst",
    model=MODEL,
    description="Evaluates patient vitals, lab values, and diagnoses to identify clinical risk levels.",
    instruction="Analyze vital signs, lab values (e.g., HbA1c, BNP, BP, SpO2), and medical notes to flag severe/moderate clinical risk factors."
)

followup_analyst = LlmAgent(
    name="followup_analyst",
    model=MODEL,
    description="Identifies missed appointments and creates prioritized care management follow-up plans.",
    instruction="Formulate prioritized outreach recommendations and follow-up care actions for high-risk patients or those who missed appointments.",
    tools=[FunctionTool(get_missed_appointment_patients), FunctionTool(get_high_risk_patients)]
)

# --- 4. Main Coordinator Agent ---
medicare_coordinator = LlmAgent(
    name="medicare_coordinator",
    model=MODEL,
    description="Orchestrates patient risk analysis and follow-up action planning.",
    instruction=(
        "You are an AI Care Coordination Agent for MediCare Clinic. "
        "Orchestrate tool calls to analyze patient records, identify patients with missed "
        "appointments or abnormal vitals/labs, and generate actionable, prioritized care follow-up plans."
    ),
    output_key="medicare_coordinator_output",
    tools=[
        FunctionTool(get_patient_record),
        FunctionTool(get_missed_appointment_patients),
        FunctionTool(get_high_risk_patients)
    ]
)

root_agent = medicare_coordinator