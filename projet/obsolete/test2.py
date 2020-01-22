
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
clientMongo = MongoClient('mongodb://localhost:27017')
database = clientMongo.aquaponey

data = {'name' : 'waterLevelSensor_1','type' : 'water','classification' : 'waterLevel','environment' : 'water','number': 1,'readOutPin': 10,'functionState':False,'functionInterval': 0,'installed': True}
database.element.insert_one(data)
