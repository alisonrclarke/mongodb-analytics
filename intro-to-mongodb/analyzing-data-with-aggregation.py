import pymongo
import pprint

client = pymongo.MongoClient('mongodb://analytics-student:analytics-password@cluster0-shard-00-00-jxeqq.mongodb.net:27017,cluster0-shard-00-01-jxeqq.mongodb.net:27017,cluster0-shard-00-02-jxeqq.mongodb.net:27017/?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin')

trips = client.citibike.trips

# Replace XXXX with your aggregation pipeline to answer the question:
# Citibike trips that start at station id 279 end most frequently at what station id?
pipeline = [
    {
        '$match': {'start station id': 279, 'end station id': 279}
    },
    {
        '$sortByCount': "$end station id"
    },
    {
        '$limit': 1
    }
]

# print the results
for trip in trips.aggregate(pipeline):
    pprint.pprint(trip)
