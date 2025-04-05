from dataclasses import dataclass
from app.data.models.appointment import Appointment


@dataclass
class User_Appointment_Request:
    appointment = Appointment()

