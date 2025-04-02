from dataclasses import dataclass
from pymongo import MongoClient
import datetime
from app.data.models.users.user import User
from app.data.models.users.doctors import Doctor

@dataclass
class Appointment:
    id : str  = None
    patient : User = None
    doctor : Doctor = None
    appointment_details : str = None
    local_time : datetime.datetime.now() = None

    client = MongoClient("mongodb://localhost:27017")
    db = client.test_database
    collection = db.appointments
