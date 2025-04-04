from app.data.models.medical_history import Medical_History
from app.data.models.users.doctors.doctor import Doctor
from app.data.models.users.user import User
from dataclasses import dataclass


@dataclass
class Medical_History_Request:
    medical_history = Medical_History()
    patient_id : str = None
    doctor_id : str = None


