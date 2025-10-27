# Services/database.py

import motor.motor_asyncio
import os
from dotenv import load_dotenv

#  Load variables from your .env file
load_dotenv()

# Get the connection string
MONGO_URI = os.getenv("MONGO_URI")

#  Database Connection
#  Asynchronous client to connect to Mongo
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

#  Select the database to use from your server instance.
db = client["Fredrick_Memory"]

# References to the "collections"
nicknames_collection = db["nicknames"]
remeber_collection = db["remember"]