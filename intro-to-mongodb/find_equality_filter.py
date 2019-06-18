import pymongo
from pymongo import MongoClient
import pprint
import re
from IPython.display import clear_output

# Replace XXXX with your connection URI from the Atlas UI
client = MongoClient("mongodb+srv://analytics:<PASSWORD>@mycluster-9jkih.mongodb.net/mflix?retryWrites=true&w=majority")

filter = {'language': 'Korean, English', 'rating': 'UNRATED'}

clear_output()
pprint.pprint(list(client.mflix.movies_initial.find(filter)))
