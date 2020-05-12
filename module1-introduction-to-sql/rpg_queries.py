
import os
import sqlite3
import pandas as pd

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")


connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)


"""
 How many total Characters are there?
 302
- How many of each specific subclass?
Cleric - 75
Fighter - 68
Mage - 108
Necromancer - 11
Thief - 51
- How many total Items?
174
- How many of the Items are weapons? How many are not?
37 are weapons, 137 are not
- How many Items does each character have? (Return first 20 rows):

SELECT 
character_id,
count(distinct item_id)
FROM charactercreator_character_inventory
GROUP BY character_id limit 20

1	3
2	3
3	2
4	4
5	4
6	1
7	5
8	3
9	4
10	4
11	3
12	3
13	4
14	4
15	4
16	1
17	5
18	5
19	3
20	1
- How many Weapons does each character have? (Return first 20 rows)

SELECT 
character_id,
count(distinct item_id)
FROM charactercreator_character_inventory
WHERE item_id between 137 and 175
GROUP BY character_id limit 20

47	1
5	2
7	1
11	1
20	1
22	1
23	1
26	1
27	3
29	2
30	1
32	1
34	1
35	2
36	3
37	2
38	2
39	2
40	1
41	1

- On average, how many Items does each Character have?
select avg(items) from (select character_id, count(item_id) as items
FROM charactercreator_character_inventory
group by character_id)

2.97 average items


group by character then select it, count items
- On average, how many Weapons does each character have?
select avg(items) from (select character_id, count(item_id) as items
FROM charactercreator_character_inventory where item_id between 137 and 175
group by character_id)

1.33974358974359
"""


class_query = """SELECT count(character_id)
from charactercreator_character"""

class_counts_query = """SELECT count(character_ptr_id)
from charactercreator_cleric"""

total_items = """SELECT count(*)
from armory_item
"""

#not doing this for every class

items_wpns = """SELECT count(*)
from armory_item 
where item_id between 137 and 175
"""

items_count = """
SELECT 
character_id,
count(distinct item_id)
FROM charactercreator_character_inventory
GROUP BY character_id limit 20
"""


item_avg = """
select avg(items) from (select character_id, count(item_id) as items
FROM charactercreator_character_inventory
group by character_id)
"""

wpn_avg = """
-- On average, how many Weapons does each character have? 
-- one single row with the avg as a single col
SELECT 
  count(distinct character_id) as character_count -- 302
  ,avg(item_count) as avg_items -- 2.97
  ,avg(weapon_count) as avg_weapons -- 0.67
FROM (
    -- row per character (302 rows)
    -- one col for the char id, one for the char name, third for the weapon count
    SELECT 
      ch.character_id
      ,ch."name" as char_name
      -- ,inv.id 
      ,count(distinct inv.item_id) as item_count
      ,count(distinct w.item_ptr_id) as weapon_count
    FROM charactercreator_character ch
    LEFT JOIN charactercreator_character_inventory inv ON ch.character_id = inv.character_id
    LEFT JOIN armory_weapon w ON inv.item_id = w.item_ptr_id
    GROUP BY 1,2
)
"""

result1 = cursor.execture(class_query).fetchall()
result2 = cursor.execute(class_counts_query).fetchall()
result3 = cursor.execute(total_items).fetchall()
result4 = cursor.execute(items_wpns).fetchall()
result5 = cursor.execute(items_count).fetchall()
result6 = cursor.execute(item_avg).fetchall()
result7 = cursor.execute(wpn_avg).fetchall()