from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
db = client.test_database
collection = db.medical_history
