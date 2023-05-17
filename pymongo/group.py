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
# Select accounts with balances of less than $1000.
select_by_balance = {"$match": {"balance": {"$lt" : 1000}}}

# Separate documents by account type and calculate the average balance for each account type.
separate_by_account_calculate_avg_balance = {"$group" : {"_id" : "$account_type", "avg_balance" : {"$avg" : "$balance"}}}

# Create an aggegation pipeline using 'stage_match_balance' and 'stage_group_account_type'.
pipeline = [
    select_by_balance,
    separate_by_account_calculate_avg_balance,
]

# Perform an aggregation on 'pipeline'.
results = accounts_collection.aggregate(pipeline)

print()
print("Average balance of checking and savings accounts with balances of less than $1000:", "\n")

for item in results:
    pprint.pprint(item)

client.close()