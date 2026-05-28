def get_appoitment(patient_id):
    appointments = {
        1:{
            "Doctor" : "Dr james",
            "Time" : "5pm"

        },
        2:{
            "Doctor": "Dr Mary",
            "Time" : "tomorow"
        }
    }

    return appointments.get(patient_id)