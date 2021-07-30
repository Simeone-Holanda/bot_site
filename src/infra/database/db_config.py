from pymongo import MongoClient

client = client_connection = MongoClient("mongodb://127.0.0.1:27017/")
base_db = client["Bot_site"]
