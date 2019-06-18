import pymongo
from pymongo import MongoClient
import pprint
from IPython.display import clear_output

# Replace XXXX with your connection URI from the Atlas UI
client = MongoClient("mongodb+srv://analytics:<PASSWORD>@mycluster-9jkih.mongodb.net/mflix?retryWrites=true&w=majority")

# pipeline = [
#     {
#         '$group': {
#             '_id': {"language": "$language"},
#             'count': {'$sum': 1}
#         }
#     },
#     {
#         '$sort': {'count': -1}
#     }
# ]

pipeline = [
    {
        '$sortByCount': "$language"
    }
]

clear_output()
pprint.pprint(list(client.mflix.movies_initial.aggregate(pipeline)))
