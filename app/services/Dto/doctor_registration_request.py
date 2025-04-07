from app.data.models.users.doctors.doctor import Doctor
from app.data.models.users.doctors.doctor_profile import Doctor_Profile
from dataclasses import dataclass

@dataclass
class Doctor_Registration_Request:
    doctor = Doctor()
    doctor_profile = Doctor_Profile()
