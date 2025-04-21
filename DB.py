from pymongo import MongoClient
from dotenv import load_dotenv
import os


def get_db_connection():
    load_dotenv()  # Load the .env file

    uri = os.getenv("MongoURI")
    if not uri:
        raise Exception("MongoURI not found. Check your .env file or environment variables.")

    # Connect to the MongoDB instance
    client = MongoClient(uri)
    db = client["Test1"]
    return db["Cluster0"]  # Return the collection+


def InsertUser(user, hashedpass, salt):
    Stuff = get_db_connection()
    Stuff.insert_one({"UserName": user, "HashedPassword": hashedpass, "Salt": salt})

def UserExists(usern):
    Stuff = get_db_connection()
    return Stuff.find_one({"UserName":usern}) is not None
def GetHash(Usertocheck):
    Stuff = get_db_connection()
    user = Stuff.find_one({"UserName": Usertocheck})
    if user:
        return user["Salt"]
    else:
        return None
def PassMatch(username, password):
    Stuff = get_db_connection()
    return Stuff.find_one({"UserName": username, "HashedPassword": password}) is not None

