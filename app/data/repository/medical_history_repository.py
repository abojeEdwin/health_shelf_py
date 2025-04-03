from abc import ABC, abstractmethod
from importlib.metadata import pass_none

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
        medical_history_dict = {
            "user_name" : medical_history.patient.user_name,
            "email" : medical_history.patient.email,
            "password" : cls.hash_password(medical_history.patient.pass_word),
            "patient_profile" :{
                "first_name" : medical_history.patient.user_profile.first_name,
                "last_name" : medical_history.patient.user_profile.last_name,
                "gender" : medical_history.patient.user_profile.gender.value,
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
                "gender" : medical_history.doctor.doctor_profile.gender.value,
                "address" : medical_history.doctor.doctor_profile.address,
                "age" : medical_history.doctor.doctor_profile.age,
                "phone_number" : medical_history.doctor.doctor_profile.phone_number,
            "doctor_specialty" :{
                "specialty": medical_history.doctor.doctor_profile.specialty.specialty,
            }
            }
            }
            }
        }
        inserted_id = db.doctors.insert_one(medical_history_dict).inserted_id
        medical_history.id = inserted_id
        return medical_history


    @classmethod
    def hash_password(cls, pass_word):
        if isinstance(pass_word, str):
            pass_word = pass_word.encode('utf-8')
        hashed_password = bcrypt.hashpw(pass_word, bcrypt.gensalt())
        return hashed_password


