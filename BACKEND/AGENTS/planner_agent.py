from TOOLS.patient_tool import get_patient_data
from TOOLS.Appointment_tool import get_appoitment
from TOOLS.AI_reasoning_tool import analyse_patient
from EVALUATIONS.rubric_engine import evaluete_response


def run_agent(patient_id):
    patient = get_patient_data(patient_id)
    appointment = get_appoitment(patient_id)
    evaluation = evaluete_response()
    result = analyse_patient(
        patient,
        appointment
    )

    return {
        "patient": patient["name"],
        "analysis" : result,
        "evaluation" : evaluation
    }


