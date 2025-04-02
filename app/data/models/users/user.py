from dataclasses import dataclass
from pymongo import MongoClient
from app.data.models.users.user_profile import User_Profile


@dataclass
class User:
    id : str = None
    user_name : str = None
    email : str =  None
    pass_word : str = None
    user_profile : User_Profile = None

    client = MongoClient("mongodb://localhost:27017")
    db = client.test_database
    collection = db.users
