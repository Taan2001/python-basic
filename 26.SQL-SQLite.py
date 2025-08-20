"""
    SQL - SQLite
"""
import sqlite3

# create connection to DB
conn = sqlite3.connect("example.db")

# create cursor object => always create it
cursor = conn.cursor()

# delete table
cursor.execute("""
DROP TABLE IF EXISTS STUDENTS
""")

# commit change
conn.commit()

# create table in DB
cursor.execute("""
CREATE TABLE IF NOT EXISTS STUDENTS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    AGE INTEGER,
    GRADE TEXT 
)
""")

# insert records
cursor.execute("""
INSERT INTO STUDENTS (NAME, AGE, GRADE)
VALUES  ('TAAN', 25, '5B'),
        ('Alica', 20, '5A')
""")

my_list = [('Bob', 15, 'A'), ('Alice', 17, 'B'), ('John', 16, 'C') ]
cursor.executemany("""
INSERT INTO STUDENTS (NAME, AGE, GRADE)
VALUES (?, ?, ?)
""", my_list)


# commit change
conn.commit()

# query
cursor.execute("SELECT * FROM STUDENTS")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("SELECT NAME, GRADE FROM STUDENTS WHERE AGE > 16")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update data
cursor.execute("""
UPDATE STUDENTS
SET NAME = "Anton"               
WHERE NAME = 'TAAN'
""")

# DELETE
cursor.execute("""
DELETE FROM STUDENTS              
WHERE NAME = 'Bob'
""")

# commit change
conn.commit()

# disconnection
conn.close()
