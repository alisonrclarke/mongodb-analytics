import pymongo
from collections import OrderedDict
from pymongo import MongoClient
import pprint
from IPython.display import clear_output

# Replace XXXX with your connection URI from the Atlas UI
client = MongoClient("mongodb+srv://analytics:<PASSWORD>@mycluster-9jkih.mongodb.net/mflix?retryWrites=true&w=majority")

pipeline = [
    {
        '$sortByCount': "$language"
    },
    {
        '$facet': {
            'top language combinations': [{'$limit': 100}],
            'unusual combinations shared by': [{
                '$skip': 100
            },
            {
                '$bucketAuto': {
                    'groupBy': "$count",
                    'buckets': 5,
                    'output': {
                        'language combinations': {'$sum': 1}
                    }
                }
            }]
        }
    }
]

clear_output()
pprint.pprint(list(client.mflix.movies_initial.aggregate(pipeline)))
