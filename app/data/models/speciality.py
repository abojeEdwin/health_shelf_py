from dataclasses import dataclass
from pymongo import MongoClient


@dataclass
class Speciality:
    id : str = None
    specialty : str = None


    client = MongoClient("mongodb://localhost:27017")
    db = client.test_database
    collection = db.specialities
