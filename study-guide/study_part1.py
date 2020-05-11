import sqlite3

connection = sqlite3.connect('study_part1.sqlite3')

table_1 = '''
CREATE TABLE table_1(
    student VARCHAR(20),
    studied VARCHAR(20),
    grade INT,
    age INT,
    sex VARCHAR(20)
);
'''

insert_1 = '''
INSERT INTO table_1
    (student, studied, grade, age, sex) 
VALUES
    ('Lion-O', 'True', 85, 24, 'Male'),
    ('Cheetara', 'True', 95, 22, 'Female'),
    ('Mumm-Ra', 'False', 65, 153, 'Male'),
    ('Snarf', 'False', 70, 15, 'Male'),
    ('Panthro', 'True', 80, 30, 'Male');
'''
