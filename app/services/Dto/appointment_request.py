from dataclasses import dataclass

from app.data.models.appointment import Appointment
from app.data.models.users.user import User
from app.data.models.users.doctors.doctor import Doctor

@dataclass
class User_Appointment_Request:
    appointment = Appointment()
    user = User()
    doctor = Doctor()
