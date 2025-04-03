from dataclasses import dataclass
import datetime
from app.data.models.users.user import User
from app.data.models.users.doctors.doctor import Doctor

@dataclass
class Appointment:
    id : str  = None
    patient : User = None
    doctor : Doctor = None
    appointment_details : str = None
    local_time : datetime.datetime.now() = None
