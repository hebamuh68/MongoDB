from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the value of the MONGO_URL environment variable
MONGODB_URL = os.environ["MONGODB_URL"]

# Connect to MongoDB
client = MongoClient(MONGODB_URL)

# List the names of all databases in the MongoDB cluster
for db_name in client.list_database_names():
    print(db_name)

# Close the MongoDB connection
client.close()
