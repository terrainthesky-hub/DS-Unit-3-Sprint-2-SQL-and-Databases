import psycopg2, sqlite3, sys
from dotenv import load_dotenv 
import os
from psycopg2.extras import execute_values
load_dotenv() #> loads contents of the .env file into the script's environment
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

schema = """CREATE TABLE charactercreator_character (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    level INTEGER,
    exp INTEGER,
    hp INTEGER,
    strength INTEGER,
    intelligence INTEGER,
    dexterity INTEGER,
    wisdom INTEGER

);
"""

conpg = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD,
                               host=DB_HOST)
curpg = conpg.cursor()

# curpg.execute(schema)
consq=sqlite3.connect('rpg_db.sqlite3')

query = """
SELECT * FROM charactercreator_character
"""
character_data = consq.execute(query).fetchall()

insertion_query = f"""
INSERT INTO charactercreator_character (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES %s
"""

execute_values(curpg, insertion_query, character_data)
conpg.commit()