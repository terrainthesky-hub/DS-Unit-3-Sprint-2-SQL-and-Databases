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

group by character then select it, count items
- On average, how many Weapons does each character have?