import psycopg2, sqlite3, sys
from dotenv import load_dotenv 
import os
from psycopg2.extras import execute_values
#Change these values as needed
load_dotenv() #> loads contents of the .env file into the script's environment
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
pgschema="""CREATE TABLE armory_item (
item_id SERIAL PRIMARY KEY,
name VARCHAR(30),
value INTEGER,
weight INTEGER);"""
consq=sqlite3.connect('rpg_db.sqlite3')
cursq=consq.cursor()
conpg = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD,
                               host=DB_HOST)
curpg = conpg.cursor()
query = """
SELECT * FROM armory_item
"""
armory_data = consq.execute(query).fetchall()
#def convert(list): 
#    return tuple(i for i in list) 
#armory_data = convert(armory_data)
insertion_query = f"""
INSERT INTO armory_item (item_id, name, value, weight) VALUES %s
"""
execute_values(curpg, insertion_query, armory_data)
conpg.commit()