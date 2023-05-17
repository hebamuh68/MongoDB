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
# Filter
""" document_to_update = {"_id": ObjectId("64518b34a4b7a98d59078fd3")}

# Updatem, inc: will increase the balance by 100
add_to_balance = {"$inc": {"balance": 100},}

# Print original document
pprint.pprint(accounts_collection.find_one(document_to_update))

# Write an expression that adds to the target account balance by the specified amount.
result = accounts_collection.update_one(document_to_update, add_to_balance)
print("Documents updated: " + str(result.modified_count))

# Print updated document
pprint.pprint(accounts_collection.find_one(document_to_update))

client.close() """

# ===========================================================
# Filter
select_accounts = {"account_type": "savings"}

# Update
set_field = {"$set": {"minimum_balance": 100}}

# Write an expression that adds a 'minimum_balance' field to each savings acccount and sets its value to 100.
result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts))

client.close()