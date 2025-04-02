from dataclasses import dataclass
from app.data.models.users.doctors.doctor_profile import Doctor_Profile
from pymongo import MongoClient


@dataclass
class Doctor:
    id : str = None
    email : str = None
    user_name : str = None
    password : str = None
    doctor_profile : Doctor_Profile = None



    client = MongoClient("mongodb://localhost:27017")
    db = client.test_database
    collection = db.doctors