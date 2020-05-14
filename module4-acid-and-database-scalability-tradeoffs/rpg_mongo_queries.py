import psycopg2, sqlite3, sys
from dotenv import load_dotenv 
import os
from psycopg2.extras import execute_values
import pandas as pd
from sqlalchemy import create_engine
import pymongo
import json

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")
#MONGO_URL = os.getenv("MONGO_URL", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
#Change these values as needed

client = pymongo.MongoClient(connection_uri)

db = client.rpg_db

armory= db.armory_item

weapon = db.armory_weapon

character = db.chractercreator_character

inventory = db.chractercreator_character_inventory

cleric = db.charactercreator_character_cleric

fighter = db.charactercreator_character_fighter

mage = db.charactercreator_character_mage

necromancer = db.charactercreator_character_necromancer

thief = db.charactercreator_character_thief


magecount = mage.count_documents({})
fightercount = fighter.count_documents({})
clericcount = cleric.count_documents({})
necrocount = necromancer.count_documents({})
thiefcount = thief.count_documents({})
# - How many total Characters are there?
totalcount = magecount + fightercount + clericcount + necrocount + thiefcount
print(totalcount)
#313

# - How many of each specific subclass?

#^

# - How many total Items?

armorycount = armory.count_documents({})
print(armorycount)

# - How many of the Items are weapons? How many are not?

weaponcount = armory.count_documents({"item_id": {"$lt": 175, '$gt': 137}})
print(weaponcount)
# - How many Items does each character have? (Return first 20 rows)

inventory_count = inventory.contest.aggregate([
    {"$group": {_id:{'$character_id'}, count:{'$sum':1}}}
])

print(inventory_count)

# - How many Weapons does each character have? (Return first 20 rows)

weapon_count_char = inventory.contest.aggregate([
    {"item_id": {"$lt": 175, '$gt': 137}},
    {"$limit": 20},
    {"$group": {_id:{'character_id'}}, count:{'$sum':1}}
])

breakpoint()
# - On average, how many Items does each Character have?
# - On average, how many Weapons does each character have?