# Ben Rudinski - Topher's Lovers
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2024

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

# create students table if it doesnt exist
c.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,  # 'id' is the unique identifier (PRIMARY KEY)
    name TEXT,               # 'name' is a text field
    age INTEGER              # 'age' is an integer field
);
''')

with open('students.csv', newline="") as csvfile:
    reader = csv.DictReader(csvfile) # read the file
    for row in reader:
        c.execute('INSERT INTO students (id, name, age) VALUES (?, ?, ?)', 
                  (row['id'], row['name'], row['age']))  # 'row' is a dictionary of column names to values

# create courses table if not exist
c.execute('''
CREATE TABLE IF NOT EXISTS courses (
    student_id INTEGER,       # This links to the student's id in the 'students' table
    code TEXT,                # 'code' represents the course name
    mark INTEGER,             # 'mark' represents the student's grade
    FOREIGN KEY(student_id) REFERENCES students(id)  # Ensure that student_id matches an entry in the 'students' table
);
''')

with open('courses.csv', newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute('INSERT INTO courses (student_id, code, mark) VALUES (?, ?, ?)', 
                  (row['id'], row['code'], row['mark']))  # values come from the CSV columns: id, code, and mark

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
