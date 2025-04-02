from dataclasses import dataclass
from app.data.models.doctors.doctor_profile import Doctor_Profile
from pymongo import MongoClient


@dataclass
class Doctor:
    id = str
    email = str
    user_name = str
    password = str
    doctor_profile = Doctor_Profile

    client = MongoClient("mongodb://localhost:27017")
    db = client.test_database
    collection = db.doctors
