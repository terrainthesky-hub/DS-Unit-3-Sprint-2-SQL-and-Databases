#Goal: insert titanic.csv file into a table in PG db.


import os
import json
import psycopg2
from dotenv import load_dotenv
import pandas as pd
from psycopg2.extras import execute_values

# adds the contents of the .env file to our environment
# looking in the .env file for env vars
load_dotenv()

import numpy as np
from psycopg2.extensions import register_adapter, AsIs
psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print(type(connection)) #> <class 'psycopg2.extensions.connection'>

cursor = connection.cursor()
print(type(cursor)) #> <class 'psycopg2.extensions.cursor'>

table_creation_query = """
DROP TABLE IF EXISTS passengers;
CREATE TABLE IF NOT EXISTS passengers (
    id SERIAL PRIMARY KEY,
    survived integer,
    pcclass integer,
    name varchar not null,
    gender varchar not null,
    age float,
    sib_spouse_count integer,
    parent_child_count integer,
    fare float
);
"""

# Survived,Pclass,Name,Sex,Age,Siblings/Spouses Aboard,Parents/Children Aboard,Fare

cursor.execute(table_creation_query)

df = pd.read_csv('titanic.csv')

print(df.head())
#h/t:

df.to_records(index=False)

rows_to_insert = list(df.to_records(index=False))

# def converted(row):
#     return ()

# rows_to_insert = [converted(row) for row in rows_to_insert]


insertion_query = "INSERT INTO passengers (survived, pcclass, name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, rows_to_insert)

connection.commit()