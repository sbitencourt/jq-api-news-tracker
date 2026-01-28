import os
import sys
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure
from dotenv import load_dotenv
from utils import get_env_path

# 1. Load Environment Variables
env_path = get_env_path()
load_dotenv(dotenv_path=env_path)

def get_db_client() -> MongoClient:
    """
    Establishes a connection to the MongoDB instance.

    Returns:
        MongoClient: The authenticated client instance.
    """
    mongo_uri = os.getenv("MONGO_URI")
    client = MongoClient(mongo_uri)
    return client

def init_database():
    """
    Performs the one-time setup for the Database.
    
    Responsibilities:
    1. Creates the Collections (Bronze and Silver).
    2. Creates Indexes (specifically the Unique Index for URLs in Silver).
    """
    client = get_db_client()
    db = client["news_datalake"] # Database Name

    # --- BRONZE LAYER ---
    db.create_collection('news_bronze')

    # --- SILVER LAYER  ---
    db.create_collection('news_silver')
    
    # Create Unique Index on 'url'
    # This ensures we never have duplicate news in the Silver layer
    db['news_silver'].create_index([("url", pymongo.ASCENDING)], unique=True)

    # Show databases and collections
    print(client.list_database_names())
    print(db.list_collection_names())

if __name__ == "__main__":
    init_database()