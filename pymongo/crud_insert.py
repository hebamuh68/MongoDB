import datetime

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the value of the MONGO_URL environment variable
MONGODB_URL = os.environ["MONGODB_URL"]

# Connect to MongoDB
client = MongoClient(MONGODB_URL)

#get reference to 'bank' database
db = client.bank

#get reference to 'accounts' collection
accounts_collection = db.accounts


# ===========================================================
new_account = {
    "account_holder":"Ziad hashim",
    "account_is":"MDZZ29001337",
    "account_type":"savings",
    "balance":50,
    "last_updated": datetime.datetime.utcnow(),
}

#insert in collection
result = accounts_collection.insert_one(new_account)

document_id = result.inserted_id
print(f"_id of inserted document: {document_id}")

client.close()