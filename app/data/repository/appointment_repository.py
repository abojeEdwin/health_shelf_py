from abc import ABC, abstractmethod

from bson import ObjectId
from pymongo import MongoClient

from app.data.models import appointment
from migrations.appointment_database import db
from app.data.models.appointment import Appointment
import bcrypt

def repository(cls):
    cls.__is_repository__ = True
    return cls

@repository
class AppointmentRepository(ABC):

    def __init__(self, client : MongoClient,db_name, appointment : Appointment):
        self.client = client
        self.db = client[client.test_database]
        self.collection = self.db[db_name.appointments]

    @classmethod
    def save(cls, appointment : Appointment) -> Appointment:
        appointment_dict = {
            "appoint_details": appointment.appointment_details,
            "user_name" :appointment.patient.user_name,
            "email" : appointment.patient.email,
            "pass_word" : cls.hash_password(appointment.patient.pass_word),
            "patient_profile" : {
                "first_name" : appointment.patient.user_profile.first_name,
                "last_name" : appointment.patient.user_profile.last_name,
                "gender" : appointment.patient.user_profile.gender.value,
                "phone_number" : appointment.patient.user_profile.phone_number,
                "address" : appointment.patient.user_profile.address,
                "age" : appointment.patient.user_profile.age,
            "doctor":{
                "user_name" : appointment.doctor.user_name,
                "email" : appointment.doctor.email,
                "pass_word" : cls.hash_password(appointment.doctor.password),
            "doctor_profile" : {
                "first_name" : appointment.doctor.doctor_profile.first_name,
                "last_name" : appointment.doctor.doctor_profile.last_name,
                "gender" : appointment.doctor.doctor_profile.gender.value,
                "phone_number" : appointment.doctor.doctor_profile.phone_number,
                "address" : appointment.doctor.doctor_profile.address,
                "age" : appointment.doctor.doctor_profile.age,
                "specialty" : appointment.doctor.doctor_profile.specialty,
            }
            }
            }
        }

        inserted_id = db.appointments.insert_one(appointment_dict).inserted_id
        appointment.id = inserted_id
        return appointment

    @classmethod
    def count_documents(cls):
        return db.appointments.count_documents({})

    @classmethod
    def hash_password(cls, password):
        if isinstance(password, str):
            password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed_password

    @classmethod
    def delete_appointment(cls, appointment : Appointment) -> bool:
        result = db.appointments.delete_one({"_id": appointment.id})
        return result.deleted_count > 0

    @classmethod
    def update(cls, appointment : Appointment) -> bool:
        appointment_dict_update = {
            "appoint_details": appointment.appointment_details,
            "user_name": appointment.patient.user_name,
            "email": appointment.patient.email,
            "pass_word": cls.hash_password(appointment.patient.pass_word),
            "patient_profile": {
                "first_name": appointment.patient.user_profile.first_name,
                "last_name": appointment.patient.user_profile.last_name,
                "gender": appointment.patient.user_profile.gender.value,
                "phone_number": appointment.patient.user_profile.phone_number,
                "address": appointment.patient.user_profile.address,
                "age": appointment.patient.user_profile.age,
                "doctor": {
                    "user_name": appointment.doctor.user_name,
                    "email": appointment.doctor.email,
                    "pass_word": cls.hash_password(appointment.doctor.password),
                    "doctor_profile": {
                        "first_name": appointment.doctor.doctor_profile.first_name,
                        "last_name": appointment.doctor.doctor_profile.last_name,
                        "gender": appointment.doctor.doctor_profile.gender.value,
                        "phone_number": appointment.doctor.doctor_profile.phone_number,
                        "address": appointment.doctor.doctor_profile.address,
                        "age": appointment.doctor.doctor_profile.age,
                        "specialty": appointment.doctor.doctor_profile.specialty,
                    }
                }
            }
        }
        inserted_id = db.appointments.update_one({"_id": appointment.id}, {"$set": appointment_dict_update})
        return inserted_id.modified_count > 0

    @classmethod
    def find_by_id(cls, id) -> Appointment:
        result = db.appointments.find_one({"_id": ObjectId(id)})
        if result:
            appointment = Appointment()
            appointment.id = result["_id"]
            return appointment
        return None


