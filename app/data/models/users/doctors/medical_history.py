from dataclasses import dataclass
from pymongo import MongoClient
from app.data.models.users.doctors.doctor import Doctor
from app.data.models.users.user import User


@dataclass
class Medical_History:
    id : str = None
    patient : User = None
    medical_history_details : str = None
    doctor : Doctor = None



    client = MongoClient("mongodb://localhost:27017")
    db = client.test_database
    collection = db.medical_history
