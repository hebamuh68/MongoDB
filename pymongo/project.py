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
# To calculate the balance in GBP, divide the original balance by the conversion rate
conversion_rate_usd_to_gbp = 1.3

# Select checking accounts with balances of more than $1,500.
select_accounts = {"$match": {"account_type": "checking", "balance": {"$gt": 200}}}

# Organize documents in order from highest balance to lowest.
organize_by_original_balance = {"$sort":{"balance":-1}}

# Return only the account type & balance fields, plus a new field containing balance in Great British Pounds (GBP).
return_specified_fields = { 
    "$project": {
        "account_type": 1,
        "balance": 1,
        "gbp_balance": { "$divide": ["$balance", conversion_rate_usd_to_gbp]},
        "_id": 0,
    }
}

# Create an aggegation pipeline containing the four stages created above
pipeline = [
    select_accounts,
    organize_by_original_balance,
    return_specified_fields,
]

# Perform an aggregation on 'pipeline'.
results = accounts_collection.aggregate(pipeline)

print(
    "Account type, original balance and balance in GDP of checking accounts with original balance greater than $1,500,"
    "in order from highest original balance to lowest: ", "\n"
)

for item in results:
    pprint.pprint(item)

client.close()