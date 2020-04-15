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

client = pymongo.MongoClient(connection_uri)

consq=sqlite3.connect('rpg_db.sqlite3')

engine = create_engine(r'sqlite:///C:\Users\lesle\Desktop\Lambda_sql_sprint\DS-Unit-3-Sprint-2-SQL-and-Databases\module3-nosql-and-document-oriented-databases\rpg_db.sqlite3')


df = pd.read_sql(query, con=engine)
armory_data = consq.execute(query).fetchall()
#armory_data = armory_data.to_json(orient='records')
#df = df.to_dict()


db = client.rpg_db
armory = db.rpg_armory

# df = pd.Series(df).apply(eval)
# df2 = pd.DataFrame(df.tolist(), columns=['item_id', 'name', 'value', 'weight'])
records = json.loads(df.T.to_json()).values()
armory.insert(records)

breakpoint()
armory.insert_many(df)

equip = armory.find_one({"name": "Qui"})
