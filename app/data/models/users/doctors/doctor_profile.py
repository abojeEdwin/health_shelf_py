from dataclasses import dataclass
from app.data.models.gender import Gender
from app.data.models.speciality import Speciality

@dataclass
class Doctor_Profile:
    id : str = None
    first_name : str = None
    last_name : str = None
    age : str = None
    gender : Gender = None
    specialty : Speciality = None
    phone_number : str = None
    address : str = None

