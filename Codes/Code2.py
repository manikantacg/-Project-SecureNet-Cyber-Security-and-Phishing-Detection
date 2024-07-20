import sqlite3
# Establishing a connection to a library database
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Creating a database of students with library access
def create_students_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                      student_id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      access_level TEXT NOT NULL)''')
    conn.commit()

def insert_student_data():
    students = [('Alice', 'Full'), ('Bob', 'Limited'), ('Charlie', 'Full')]
    cursor.executemany('''INSERT INTO students (name, access_level)
                          VALUES (?, ?)''', students)
    conn.commit()

def fetch_students_data():
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Create table and insert student data
create_students_table()
insert_student_data()
fetch_students_data()

# Close the connection
conn.close()
