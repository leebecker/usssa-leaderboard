from bson import ObjectId
from pymongo import MongoClient
import motor.motor_asyncio
import os
from usssa_leaderboard.config import settings

#db_connection = MongoClient("mongodb://localhost:27017")
#db = db_connection.database_name
#collection = db["collection_name"]

DB_NAME = "leaderboard_db"

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
db = client[DB_NAME]
print('🚀 Connected to MongoDB...')


class PyObjectId(ObjectId):
    """Schema for ObjectId"""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

#from pymongo import MongoClient
#import settings

#client = MongoClient(settings.mongodb_uri, settings.port)
#db = client[customerdata]
