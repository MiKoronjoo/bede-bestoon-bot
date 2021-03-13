from pymongo import MongoClient
from pymongo.database import Database


class Entity:
    @staticmethod
    def db() -> Database:
        mongo_client = MongoClient('localhost', 27017)
        database = mongo_client.bedebestoon
        return database
