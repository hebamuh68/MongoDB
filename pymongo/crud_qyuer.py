import datetime
import pprint

from pymongo import MongoClient
from dotenv import load_dotenv
from bson.objectid import ObjectId

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
# Query by ObjectId
""" document_to_find = {"_id": ObjectId("64518b34a4b7a98d59078fd3")}

# Write an expression that retrieves the document matching the query constraint in the 'accounts' collection.
result = accounts_collection.find_one(document_to_find)

# this print in json format
pprint.pprint(result)

client.close() """

# ===========================================================
# Query
documents_to_find = {"balance": {"$gt": 700}}

# Write an expression that selects the documents matching the query constraint in the 'accounts' collection.
cursor = accounts_collection.find(documents_to_find)

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()
print("# of documents found: " + str(num_docs))

client.close()