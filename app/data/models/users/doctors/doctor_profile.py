from dataclasses import dataclass
from pymongo import MongoClient

from app.data.models.gender import Gender
from app.data.models.speciality import Speciality

@dataclass
class Doctor_Profile:
    id = str
    first_name = str
    last_name = str
    age = str
    gender = Gender
    specialty = Speciality
    phone_number = str
    address = str

    client = MongoClient("mongodb://localhost:27017")
    db = client.test_database
    collection = db.doctors_profile
