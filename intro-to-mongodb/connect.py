from pymongo import MongoClient

client = MongoClient("mongodb+srv://analytics:<PASSWORD>@mycluster-9jkih.mongodb.net/mflix?retryWrites=true&w=majority")
print(client.mflix)
