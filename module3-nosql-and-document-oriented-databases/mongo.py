import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

#mongodb+srv://terra:<password>@cluster0-mybxz.mongodb.net/test?retryWrites=true&w=majority
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.inclass_db_ds13 # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

breakpoint()


collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names()) #won't see until after inserting data

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
    "other_attr":{
        "a": 1,
        "b": [1,2,3]
    }
})
print("DOCS:", collection.count_documents({})) #select count(id) from pokemon
print("Pikas:", collection.count_documents({"name": "Pikachu"}))
#select count(id) from pokemon where name = 'Pikachu'