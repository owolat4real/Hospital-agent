def get_patient_data(patient_id):
    patients = {
        1:{
            "name" : "john",
            "oxygen" : 82,
            "BP" : "high",
            "temperature":103    
        },
        2:{
            "name":"Jane",
            "oxygen": 78,
            "BP":"low",
            "temperature": 109

        }
    }
    return patients.get(patient_id)

