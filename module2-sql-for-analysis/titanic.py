import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values
import pandas as pd
from sqlalchemy import create_engine

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
#DB_FILEPATH = ('charactercreator_character_inventory.csv')

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION:", connection)

cursor = connection.cursor()
# f = open(r'C:\Users\lesle\Desktop\Lambda_sql_sprint\DS-Unit-3-Sprint-2-SQL-and-Databases\module2-sql-for-analysis\titanic.csv', 'r')
# cursor.copy_from(f, titanic, sep=',')
# f.close()

titanic_filepath = 'titanic.csv'
df = pd.read_csv(titanic_filepath)
#breakpoint()
engine = create_engine('postgres://ylcphoaq:iK12dFvVXxwZjnB4x6F3EEIem9xxfjTd@drona.db.elephantsql.com:5432/ylcphoaq')

df.to_sql('titanic3', engine)
conn = engine.raw_connection()
conn.commit()