import pandas as pd
import os

# Resolve path to the data file relative to this file
DATA_FILE = os.path.join(os.path.dirname(__file__), "patient_data.xlsx")

def load_data():
    if not os.path.exists(DATA_FILE):
        return pd.DataFrame()
    return pd.read_excel(DATA_FILE)

df_patients = load_data()

def get_patient_record(patient_id: str) -> str:
    """Fetch clinical snapshot and details for a specific patient ID."""
    if df_patients.empty:
        return "Patient dataset not loaded."
    record = df_patients[df_patients['patient_id'].str.upper() == patient_id.upper()]
    if record.empty:
        return f"Patient ID {patient_id} not found."
    return record.to_json(orient="records")

def get_missed_appointment_patients() -> str:
    'Fetch list of patients who missed their last scheduled appointment.'
    if df_patients.empty:
        return "Patient dataset not loaded."
    missed = df_patients[df_patients['missed_last_appointment'].str.lower() == 'yes']
    return missed[['patient_id', 'patient_name', 'diagnosis', 'days_since_last_visit', 'notes']].to_json(orient="records")

def get_high_risk_patients() -> str:
    'Fetch patients with abnormal vitals or lab values (e.g. Systolic BP > 140, SpO2 < 92, HbA1c > 9.0).'
    if df_patients.empty:
        return "Patient dataset not loaded."
    high_risk = df_patients[
        (df_patients['vitals_bp_systolic'] > 140) |
        (df_patients['vitals_spo2'] < 92) |
        (df_patients['missed_last_appointment'].str.lower() == 'yes')
    ]
    return high_risk[['patient_id', 'patient_name', 'diagnosis', 'lab_test', 'lab_value', 'vitals_bp_systolic', 'vitals_spo2']].to_json(orient="records")

def get_full_dataset() -> str:
    'Return the summary of the full patient dataset for exploration.'
    if df_patients.empty:
        return "Patient dataset not loaded."
    return df_patients.to_json(orient="records")
