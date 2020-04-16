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
query = """
SELECT * FROM armory_item
"""

query2="""
SELECT * from armory_weapon
"""
query3="""
SELECT * FROM charactercreator_character
"""

query4 ="""
SELECT * FROM charactercreator_character_inventory
"""

query5 = """
SELECT * FROM charactercreator_cleric
"""

query6 = """
SELECT * FROM charactercreator_fighter
"""
query7 = """
SELECT * FROM charactercreator_mage
"""

query8 = """
SELECT * FROM charactercreator_necromancer
"""

query9 = """
SELECT * FROM charactercreator_thief
"""

client = pymongo.MongoClient(connection_uri)

#consq=sqlite3.connect('rpg_db.sqlite3')

engine = create_engine(r'sqlite:///C:\Users\lesle\Desktop\Lambda_sql_sprint\DS-Unit-3-Sprint-2-SQL-and-Databases\module3-nosql-and-document-oriented-databases\rpg_db.sqlite3')


df = pd.read_sql(query, con=engine)
df2 = pd.read_sql(query2, con=engine)
df3 = pd.read_sql(query3, con=engine)
df4 = pd.read_sql(query4, con=engine)
df5 = pd.read_sql(query5, con=engine)
df6 = pd.read_sql(query6, con=engine)
df7 = pd.read_sql(query7, con=engine)
df8 = pd.read_sql(query8, con=engine)
df9 = pd.read_sql(query9, con=engine)

db = client.rpg_db
armory= db.armory_item
records = json.loads(df.to_json())
armory.insert(records)

weapon = db.armory_weapon
records2 = json.loads(df2.to_json())
weapon.insert(records2)

character = db.chractercreator_character
records3 = json.loads(df3.to_json())
character.insert(records3)

inventory = db.chractercreator_character_inventory
records4 = json.loads(df4.to_json())
inventory.insert(records4)

cleric = db.charactercreator_character_cleric
records5 = json.loads(df5.to_json())
cleric.insert(records5)

fighter = db.charactercreator_character_fighter
records6 = json.loads(df6.to_json())
fighter.insert(records6)

mage = db.charactercreator_character_mage
records7 = json.loads(df7.to_json())
mage.insert(records7)

necromancer = db.charactercreator_character_necromancer
records8 = json.loads(df8.to_json())
necromancer.insert(records8)

thief = db.charactercreator_character_thief
records9 = json.loads(df9.to_json())
thief.insert(records9)


breakpoint()

equip = armory.find_one({"name": "Qui"})
