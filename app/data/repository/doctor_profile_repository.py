from abc import ABC, abstractmethod
from typing import List
from bson import ObjectId
from pymongo import MongoClient
from app.data.models.users.doctors.doctor import Doctor
from migrations.doctor_data_base import db
import bcrypt


def repository(cls):
    cls.__is_repository__ = True
    return cls


@repository
class DoctorRepository(ABC):
    def __init__(self, client : MongoClient,db_name, doctor : Doctor):
        self.client = client
        self.db = self.client[client.test_database]
        self.collection = self.db[db_name.doctors]

    @abstractmethod
    def _create_indexes(self):
        self.collection.create_index("email", unique=True)
        self.collection.create_index("username", unique=True)

    @classmethod
    def count_documents(cls):
        return db.doctors.count_documents({})

    @classmethod
    def save(cls, doctor : Doctor) -> Doctor:
        doctor_dict = {
            "user_name": doctor.user_name,
            "email": doctor.email,
            "password": cls.hash_password(doctor.password),
            "doctor_profile": {
                "first_name": doctor.doctor_profile.first_name,
                "last_name": doctor.doctor_profile.last_name,
                "age": doctor.doctor_profile.age,
                "gender": doctor.doctor_profile.gender.value,
                "phone_number": doctor.doctor_profile.phone_number,
                "address": doctor.doctor_profile.address,
            "doctor_specialty":{
                "specialty": doctor.doctor_profile.specialty.specialty,
            }
            }
        }
        inserted_id = db.doctors.insert_one(doctor_dict).inserted_id
        doctor.id = inserted_id
        return doctor

    @classmethod
    def delete(cls, doctor : Doctor) -> bool:
        result = db.doctors.delete_one({"_id": doctor.id})
        return result.deleted_count > 0

    @classmethod
    def update(cls, doctor : Doctor , id) -> bool:
        doctor_dict = {
            "user_name": doctor.user_name,
            "email": doctor.email,
            "password": cls.hash_password(doctor.password),
            "doctor_profile": {
                "first_name": doctor.doctor_profile.first_name,
                "last_name": doctor.doctor_profile.last_name,
                "age": doctor.doctor_profile.age,
                "gender": doctor.doctor_profile.gender.value,
                "phone_number": doctor.doctor_profile.phone_number,
                "address": doctor.doctor_profile.address,
            "specialty": {
                "specialty": doctor.doctor_profile.specialty.specialty
                }
            }
        }
        result = db.doctors.update_one(
            {"_id": ObjectId(id)},
            {"$set": doctor_dict}
        )
        return result.modified_count > 0

    @classmethod
    def exists_by_email(cls, email) -> bool:
        return db.doctors.find_one({"email": email})

    @classmethod
    def exists_by_username(cls, user_name):
        return db.doctors.find_one({"user_name": user_name})

    @classmethod
    def find_by_id(cls, id) -> Doctor:
        return db.doctors.find_one({"_id": id})

    @classmethod
    def find_by_username(cls, user_name) -> Doctor:
        result = db.doctors.find_one({"user_name": user_name})
        return result

    @classmethod
    def find_all(cls):
        return db.doctors.count_documents({})

    @classmethod
    def exists_by_id(cls, id) -> bool:
        return db.doctors.find_one({"_id": id})

    @classmethod
    def delete_by_id(cls, id) -> bool :
        return db.doctors.delete_many({"_id": ObjectId(id)})
        return result.deleted_count > 0

    @classmethod
    def delete_doctors_by_id(cls, doctors_ids) -> List[Doctor]:
        result = db.doctors.delete_many({"_id": {"$in": doctors_ids}})
        return result.deleted_count > 0

    @classmethod
    def hash_password(cls, password):
        if isinstance(password, str):
            password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed_password

    @classmethod
    def delete_all(cls):
        return db.doctors.delete_many({})


    @classmethod
    def find_by_email(cls, email: str) -> Doctor:
        doctor = db.doctors.find_one({"email":email})
        return doctor

    @classmethod
    def verify_password(cls, hashed_password: str, input_password: str) -> bool:

        if not hashed_password or not input_password:
            return False
        try:
            if isinstance(hashed_password, str):
                hashed_password_bytes = hashed_password.encode('utf-8')
            else:
                hashed_password_bytes = hashed_password
            if isinstance(input_password, str):
                input_password_bytes = input_password.encode('utf-8')
            else:
                input_password_bytes = input_password
            return bcrypt.checkpw(input_password_bytes, hashed_password_bytes)

        except (ValueError, TypeError, AttributeError) as e:
            return False

