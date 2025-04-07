import re
from abc import ABC, abstractmethod
from typing import List, Optional
from bson import ObjectId
from pymongo import MongoClient
from app.data.models.users.user import User
from migrations.doctor_data_base import db
import bcrypt


def repository(cls):
    cls.__is_repository__ = True
    return cls


@repository
class UserRepository(ABC):

    @abstractmethod
    def __init__(self, client : MongoClient,db_name, user : User):
        self.client = client
        self.db = self.client[client.test_database]
        self.collection = self.db[db_name.user_profile]

    @abstractmethod
    def _create_indexes(self):
        self.collection.create_index("email", unique=True)
        self.collection.create_index("username", unique=True)

    @classmethod
    def save(cls, user : User) -> User:
        if not cls.verify_email(user.email):
            raise TypeError("invalid email")
        user_dict = {
            "user_name": user.user_name,
            "email": user.email,
            "password": cls.hash_password(user.pass_word),
            "user_profile": {
                "first_name": user.user_profile.first_name,
                "last_name": user.user_profile.last_name,
                "age": user.user_profile.age,
                "gender": user.user_profile.gender,
                "phone_number": user.user_profile.phone_number,
                "address": user.user_profile.address,
            }
        }
        inserted_id = db.users.insert_one(user_dict).inserted_id
        user.id = inserted_id
        return user

    @classmethod
    def find_by_email(cls, email: str) -> User:
        user = db.users.find_one({"email":email})
        return user

    @classmethod
    def delete(cls, user : User) -> bool:
        result = db.users.delete_one({"_id": user.id})
        return result.deleted_count > 0

    @classmethod
    def delete_all(cls):
        db.users.delete_many({})

    @classmethod
    def find_all(cls):
        return db.users.count_documents({})

    @classmethod
    def count_documents(cls):
        return db.users.count_documents({})

    @classmethod
    def exist_by_email(cls, email) -> bool:
        return db.users.count_documents({"email": email}) > 0

    @classmethod
    def find_by_username(cls, username) -> User:
        return db.users.count_documents({"user_name": username}) > 0

    @classmethod
    def find_by_id(cls,user_id) -> User:
        return db.users.find_one({"_id": user_id})

    @classmethod
    def exists_by_username(cls, username) -> bool:
        return db.users.count_documents({"user_name": username}) > 0

    @classmethod
    def exists_by_id(cls, id) ->bool:
        return db.users.find_one({"_id": id})

    @classmethod
    def delete_by_id(cls, id) -> bool:
       result = db.users.delete_one({"_id": ObjectId(id)})
       return result.deleted_count > 0

    @classmethod
    def delete_users_by_id(cls, users_ids)-> List[User]:
        result = db.users.delete_many({"_id": {"$in": users_ids}})
        return result.deleted_count > 0

    @classmethod
    def update(cls, user : User, id) -> bool:
        if not cls.verify_email(user.email):
            raise TypeError("invalid email")

        user_dict = {
            "user_name": user.user_name,
            "email": user.email,
            "password": cls.hash_password(user.pass_word),
            "user_profile": {
                "first_name": user.user_profile.first_name,
                "last_name": user.user_profile.last_name,
                "age": user.user_profile.age,
                "gender": user.user_profile.gender,
                "phone_number": user.user_profile.phone_number,
                "address": user.user_profile.address,
            }
        }
        result = db.users.update_one({"_id": ObjectId(id)}, {"$set": user_dict})
        return result.modified_count > 0

    @classmethod
    def hash_password(cls, password):
        if not password:
            raise ValueError("Password cannot be None")
        if isinstance(password, str):
            password = password.encode('utf-8')
        return bcrypt.hashpw(password, bcrypt.gensalt())

    @classmethod
    def verify_email(cls,email : str) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$'
        try:
            if not re.match(pattern, email):
                raise TypeError("Please enter a valid email")
            return True
        except ValueError:
            print("Invalid email")



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







