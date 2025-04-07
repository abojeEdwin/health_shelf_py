import re
from abc import ABC, abstractmethod
from bson import ObjectId
from pymongo import MongoClient
from app.data.models.medical_history import Medical_History
from migrations.medical_history_database import db
import bcrypt


def repository(cls):
    cls.__is_repository__ = True
    return cls

@repository
class MedicalHistoryRepository(ABC):

    def __init__(self, client :MongoClient,db_name, medical_history : Medical_History):
        self.client = client
        self.db = self.client[client.test_database]
        self.collection = self.db[db_name.medical_history]

    @classmethod
    def count_documents(cls):
        return db.medical_history.count_documents({})

    @classmethod
    def save(cls, medical_history : Medical_History) -> Medical_History:
        if not cls.verify_email(medical_history.doctor.email):
            raise TypeError("invalid doctor email")

        medical_history_dict = {
            "medical_history_details": medical_history.medical_history_details,
            "user_name" : medical_history.patient.user_name,
            "email" : medical_history.patient.email,
            "password" : cls.hash_password(medical_history.patient.pass_word),
            "patient_profile" :{
                "first_name" : medical_history.patient.user_profile.first_name,
                "last_name" : medical_history.patient.user_profile.last_name,
                "gender" : medical_history.patient.user_profile.gender,
                "address" : medical_history.patient.user_profile.address,
                "age" : medical_history.patient.user_profile.age,
                "phone_number" : medical_history.patient.user_profile.phone_number,
            "doctor" :{
                "user_name" : medical_history.doctor.user_name,
                "email" : medical_history.doctor.email,
                "password" : cls.hash_password(medical_history.doctor.password),
            "doctor_profile" :{
                "first_name" : medical_history.doctor.doctor_profile.first_name,
                "last_name" : medical_history.doctor.doctor_profile.last_name,
                "gender" : medical_history.doctor.doctor_profile.gender,
                "address" : medical_history.doctor.doctor_profile.address,
                "age" : medical_history.doctor.doctor_profile.age,
                "phone_number" : medical_history.doctor.doctor_profile.phone_number,
            "doctor_specialty" :{
                "specialty": medical_history.doctor.doctor_profile.specialty,
            }
            }
            }
            }
        }
        inserted_id = db.medical_history.insert_one(medical_history_dict).inserted_id
        medical_history.id = inserted_id
        return medical_history


    @classmethod
    def hash_password(cls, pass_word):
        if isinstance(pass_word, str):
            pass_word = pass_word.encode('utf-8')
        hashed_password = bcrypt.hashpw(pass_word, bcrypt.gensalt())
        return hashed_password

    @classmethod
    def update(cls, medical_history: Medical_History, id: str) -> bool:
        if not cls.verify_email(medical_history.doctor.email):
            raise TypeError("invalid doctor email")
        if not cls.verify_email(medical_history.patient.email):
            raise TypeError("invalid patient email")
        update_data = {
            "medical_history_details": medical_history.medical_history_details,
            "patient": {
                "user_name": medical_history.patient.user_name,
                "email": medical_history.patient.email,
                "pass_word": cls.hash_password(medical_history.patient.pass_word),
                "user_profile": {
                    "first_name": medical_history.patient.user_profile.first_name,
                    "last_name": medical_history.patient.user_profile.last_name,
                    "gender": medical_history.patient.user_profile.gender,
                    "address": medical_history.patient.user_profile.address,
                    "age": medical_history.patient.user_profile.age,
                    "phone_number": medical_history.patient.user_profile.phone_number
                }
            },
            "doctor": {
                "user_name": medical_history.doctor.user_name,
                "email": medical_history.doctor.email,
                "password": cls.hash_password(medical_history.doctor.password),
                "doctor_profile": {
                    "first_name": medical_history.doctor.doctor_profile.first_name,
                    "last_name": medical_history.doctor.doctor_profile.last_name,
                    "gender": medical_history.doctor.doctor_profile.gender,
                    "address": medical_history.doctor.doctor_profile.address,
                    "age": medical_history.doctor.doctor_profile.age,
                    "phone_number": medical_history.doctor.doctor_profile.phone_number,
                    "specialty": {
                        "specialty": medical_history.doctor.doctor_profile.specialty
                    }
                }
            }
        }
        result = db.medical_history.update_one(
            {"_id": ObjectId(id)},
            {"$set": update_data}
        )
        return result.modified_count == 1

    @classmethod
    def find_by_id(cls, id) -> Medical_History:
        result = db.medical_history.find_one({"_id": ObjectId(id)})
        if result:
            medical_history = Medical_History()
            medical_history.id = result["_id"]
            return medical_history
        return None

    @classmethod
    def verify_email(cls, email: str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$'
        try:
            if not re.match(pattern, email):
                raise TypeError("Please enter a valid email")
            return True
        except ValueError:
            print("Invalid email")

