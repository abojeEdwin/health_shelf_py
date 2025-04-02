from dataclasses import dataclass
from app.data.models.users.doctors.doctor import Doctor
from app.data.models.users.user import User


@dataclass
class Medical_History:
    id : str = None
    patient : User = None
    medical_history_details : str = None
    doctor : Doctor = None

