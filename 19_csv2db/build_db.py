# Ben Rudinski - Topher's Lovers
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3
import csv

DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()  #facilitate db ops -- you will use cursor to trigger db events

# ==========================================================

# create 'students' table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,  -- 'id' is the unique identifier (PRIMARY KEY)
    name TEXT,               -- 'name' is a text field
    age INTEGER              -- 'age' is an integer field
);
''')

# insert students data into db
with open('students.csv', newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('INSERT OR IGNORE INTO students (id, name, age) VALUES (?, ?, ?)', 
                  (row['id'], row['name'], row['age']))

# Ccreate 'courses' table if it doesn't exist
c.execute('''
CREATE TABLE IF NOT EXISTS courses (
    student_id INTEGER,      -- links to the student's id in the 'students' table
    code TEXT,               -- 'code' represents the course name
    mark INTEGER,            -- 'mark' represents the student's grade
    FOREIGN KEY(student_id) REFERENCES students(id)  -- ensures that student_id exists in 'students' table
);
''')

# insert courses data into db
with open('courses.csv', newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('INSERT OR IGNORE INTO courses (student_id, code, mark) VALUES (?, ?, ?)', 
                  (row['id'], row['code'], row['mark']))

# ==========================================================

db.commit() #save changes
db.close() # close db