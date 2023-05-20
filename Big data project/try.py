#Create connection
from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://Al-Hassan:Bigdata1128@bigdataproject.nhz6c7e.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB_URL)

for db_name in client.list_database_names():
    print(db_name)

client.close()