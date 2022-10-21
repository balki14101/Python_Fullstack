
from pymongo import MongoClient

import urllib.parse


client = MongoClient("mongodb+srv://PythonFullstack:"+urllib.parse.quote("pythonfullstack")+"@python0.zgfrb1y.mongodb.net/?ssl=true&ssl_cert_reqs=CERT_NONE")
# client = MongoClient("mongodb+srv://PythonFullstack:"+urllib.parse.quote("pythonfullstack")+"@python0.zgfrb1y.mongodb.net/?retryWrites=true&w=majority")
conn = client.project
conn_user = client.user


