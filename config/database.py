
from pymongo import MongoClient
# import motor.motor_asyncio

import urllib.parse

# conn = MongoClient()

mongo_uri = "mongodb+srv://PythonFullstack:"+urllib.parse.quote("pythonfullstack")+"@python0.zgfrb1y.mongodb.net/?retryWrites=true&w=majority"
# client = motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
# conn = client.project

client = MongoClient("mongodb+srv://PythonFullstack:"+urllib.parse.quote("pythonfullstack")+"@python0.zgfrb1y.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE")
# client = MongoClient("mongodb+srv://PythonFullstack:"+urllib.parse.quote("pythonfullstack")+"@python0.zgfrb1y.mongodb.net/?retryWrites=true&w=majority")
conn = client.project

