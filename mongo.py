import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI) 

coll = conn[DBS_NAME][COLLECTION_NAME]



# new_docs = [{'first': 'douglas', 'last': 'adams', 'dob':'11/03/1952', 'hair_colour': 'grey', 'occupation': 'writer', 'nationality': 'english'},{'first': 'deborah', 'last': 'meaden', 'dob': '11/02/1959', 'hair_colour': 'blond', 'occupation': 'entrepreneur', 'nationality': 'english'}]

# coll.insert_many(new_docs)

# To insert

# coll.insert(new_doc)

# documents = coll.find({'nationality': 'irish'})

# coll.remove({'first': 'douglas'})

coll.update_many({'nationality': 'english'}, {'$set': {'hair_colour': 'blue'}})

documents = coll.find({'nationality':'english'})

for doc in documents:
    print(doc)

