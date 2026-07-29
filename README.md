# MediCare Assist Agent

MediCare Assist is an AI-powered healthcare coordination platform built with the Google Agent Development Kit (ADK). It orchestrates a team of specialized sub-agents to proactively manage patient care, analyze clinical risks, and coordinate follow-up actions.

## 🚀 Overview

The system is designed for healthcare coordination teams to:
- **Analyze Patient Snapshots:** Quickly retrieve and summarize clinical data, vitals, and lab results.
- **Identify Clinical Risks:** Automatically flag anomalies in vitals (e.g., Blood Pressure, SpO2) and lab values (e.g., HbA1c).
- **Manage Follow-ups:** Track missed appointments and generate prioritized outreach recommendations.
- **Prioritize Care:** Deliver actionable, clinical-grade care plans.

## 🏗️ Architecture

MediCare Assist uses an orchestration pattern with a lead coordinator agent and several expert sub-agents.

### Lead Coordinator: `medicare_coordinator`
The "brain" of the system. It receives requests and delegates tasks to specialized sub-agents to compile a comprehensive clinical report and action plan.

### Specialized Sub-Agents
- **Patient Data Analyst:** Handles data extraction from patient records and summarizes clinical history.
- **Clinical Risk Analyst:** Evaluates vitals and lab results to determine risk levels (Severe/Moderate/Stable).
- **Follow-up Analyst:** Identifies gaps in care, such as missed appointments, and formulates outreach strategies.

## 🛠️ Tech Stack
- **Framework:** Google Agent Development Kit (ADK)
- **Model:** Gemini 2.5 Pro
- **Data Handling:** Pandas (Excel-based patient registry)

## 📁 Project Structure

```text
medic_assist/
├── agent.py                # Main entry point and Coordinator definition
├── sub_agents/
│   ├── sub_agents.py       # Definitions for all sub-agents and their tools
│   ├── data_utils.py       # Helper functions for data retrieval
│   ├── patient_data.xlsx   # Patient registry (Mock data)
│   ├── clinical_risk_analyst/
│   ├── followup_analyst/
│   └── patient_data_analyst/
└── requirements.txt        # Project dependencies
```

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sharmara18/medic_assist.git
   cd medic_assist
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add your API keys (e.g., for Google Cloud/Vertex AI).

## 📊 Usage

The agent can be interacted with via the ADK interface. Example queries include:
- *"Analyze patient ID P123 and provide a clinical risk snapshot."*
- *"Who are the high-risk patients that missed their last appointment?"*
- *"Generate a follow-up action plan for patients with HbA1c > 9.0."*

---
*Disclaimer: This is a prototype system using mock data. It is intended for demonstration purposes and should not be used for actual medical decision-making without professional clinical oversight.*
