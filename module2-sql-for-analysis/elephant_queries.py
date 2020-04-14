import psycopg2
import os
from dotenv import load_dotenv
from psycopg2.extras import execute_values

load_dotenv() #> loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)

print(type(conn))
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
print(type(cur))
### An example query
cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
results = cur.fetchone()
print(results)

all_results = cur.fetchall()
print(all_results)

my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }

#insertion_query = "INSERT INTO {table_name} (name, data) VALUES (%s, %s)"
cursor.execute(insertion_query,
  ('A rowwwww', 'null')
)
cursor.execute(insertion_query,
  ('Another row, with JSONNNNN', json.dumps(my_dict))
#)

rows_to_insert = [('A rowwwww', 'null'),
    ('Another row, with JSONNNNN', json.dumps(my_dict))]

# h/t: https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query
insertion_query = "INSERT INTO {table_name} (name, data) VALUES %s"
execute_values(cursor, insertion_query, rows_to_insert)

#  ('A rowwwww', 'null'),
#  ('Another row, with JSONNNNN', json.dumps(my_dict)),
#  ('Third row', "3")

conn.commit()