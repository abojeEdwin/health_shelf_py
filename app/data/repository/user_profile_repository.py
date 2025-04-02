from abc import ABC, abstractmethod
from pymongo import MongoClient
from app.data.models.users.user import User
from migrations.doctor_data_base import db


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
        user_dict = {
            "user_name": user.user_name,
            "email": user.email,
            "password": user.pass_word,
            "user_profile": {
                "first_name": user.user_profile.first_name,
                "last_name": user.user_profile.last_name,
                "age": user.user_profile.age,
                "gender": user.user_profile.gender.value,
                "phone_number": user.user_profile.phone_number,
                "address": user.user_profile.address,
            }
        }
        inserted_id = db.users.insert_one(user_dict).inserted_id
        user.id = inserted_id
        return user





