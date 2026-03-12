# database.py

# description

# import statements
from pymongo import MongoClient

def connect_db():
    connection_string = "mongodb://localhost:27017"

    try:
        client = MongoClient(connection_string)
        db = client.mydb
        collection = db.my_collection

        print("Database connected")
    except Exception as e:
        print(f"Connection failed: {e}")

if __name__=="__main__":
    connect_db()