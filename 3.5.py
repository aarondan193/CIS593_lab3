# Requires the PyMongo package.
# https://api.mongodb.com/python/current
from pymongo import MongoClient

client = MongoClient('mongodb+srv://aaron:madcow@cluster0.incdz.mongodb.net/test?authSource=admin&replicaSet=atlas-mn4ume-shard-0&readPreference=primary&appname=MongoDB+Compass&ssl=true')
result = client['tweets']['tweets'].aggregate([
    {
        '$project': {
            'words': {
                '$split': [
                    '$data.text', ' '
                ]
            }
        }
    }, {
        '$unwind': {
            'path': '$words', 
            'includeArrayIndex': 'string', 
            'preserveNullAndEmptyArrays': False
        }
    }, {
        '$group': {
            '_id': '$words', 
            'count': {
                '$sum': 1
            }
        }
    }, {
        '$sort': {
            'count': -1
        }
    }, {
        '$limit': 50
    }
])

for word in result:
    print (word)