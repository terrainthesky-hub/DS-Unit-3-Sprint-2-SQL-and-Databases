
import os
import sqlite3
import pandas as pd

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.csv")


connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

df = pd.read_csv(DB_FILEPATH)

df.to_sql('review', con=sqlite3.connect('buddywhatever.sqlite3'))

query = """SELECT *
from review
where Nature > 100 and Shopping > 100"""

#result = cursor.execute(query)
#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)

result2 = cursor.execute(query).fetchall(df)
print("RESULT 2", result2)