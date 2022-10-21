## Kafka Consumer
import os
import pymongo
from kafka import KafkaConsumer
import sys
import json
from pathlib import Path
from config.database import mongo_uri

base_dir = Path(__file__).resolve().parent

client_priyanka = pymongo.MongoClient(mongo_uri)
# db = client.test

# bootstrap_servers = "kafka"
bootstrap_servers = 'localhost:9092'
topicName = 'transport_data'


# client = pymongo.MongoClient("mongodb://localhost:27017/")
# 1client = pymongo.MongoClient("db")  # for docker local
#client = pymongo.MongoClient(os.getenv("mongouri"))  # mongo atlas
mydb = client_priyanka["user"]
mycoll = mydb["mycol"]

try:
    consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers,auto_offset_reset = 'earliest')
    for data in consumer:
        data = json.loads(data.value)
        insert_data = mycoll.insert_one(data)
        print(insert_data)
except KeyboardInterrupt:
    sys.exit()