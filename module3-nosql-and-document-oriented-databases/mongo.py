import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = 'cluster0-mybxz'



connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.inclass_db_ds13 # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)




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



warturtle = {
"name": "Warturtle",
"level": 90,
"exp": 100,
"hp": 1000,
}

jigglypuff = {
    "name": "Jigglypuff",
    "level": 99,
    "exp": 100000000000,
    "hp": 500,
}

charizard = {
    "name": "charizard",
    "level": 30,
    "exp": 4450000000,
    "hp": 500,
    "learned_moves":{
        "flamethrower":30,
        "fly": 42
    }
}
team = [warturtle, jigglypuff, charizard]

collection.insert_many(team)





print("DOCS:", collection.count_documents({})) #select count(id) from pokemon
print("Pikas:", collection.count_documents({"name": "Pikachu"}))
#select count(id) from pokemon where name = 'Pikachu'
pika = colletion.find_one({"name": "Pikachu"})

pikas = list(collection.find_many({'name': 'Pikachu'})) #print(list(pikas)) in breakpoint terminal
print(pika)
print(pikas)

strong_pokemon = list(collection.find_many({'level': {"$gte": 70}}))
print("High level pokemon", strong_pokemon)