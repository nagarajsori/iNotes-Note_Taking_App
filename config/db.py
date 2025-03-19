from pymongo import MongoClient
from pymongo import MongoClient
from urllib.parse import quote_plus

username = "nagarajsori2003"
password = quote_plus("an!Tn8pPR!Lt@J8")  # URL-encode special characters

MONGO_URI = f"mongodb+srv://{username}:{password}@mongoyoutube.ftqo4.mongodb.net/"
conn = MongoClient(MONGO_URI)

#MONGO_URI = "mongodb+srv://nagarajsori2003:an!Tn8pPR!Lt@J8@mongoyoutube.ftqo4.mongodb.net/"
