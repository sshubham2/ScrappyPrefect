import pymongo
from src.config.context_vars import settings, ENV_VARS

class COLLECTIONS:
    COVID_RECORDS = "covid-records"

def getCollection(collection):
    return db[collection]

db = pymongo.MongoClient(settings[ENV_VARS.MONGO_URL])[settings[ENV_VARS.DB_NAME]]


