import sqlite3

# Establishing a connection to a secure database
conn = sqlite3.connect('secure_network.db')
cursor = conn.cursor()

# Simulating gaining access and manipulating data
def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS secure_data (
                      id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      value TEXT NOT NULL)''')
    conn.commit()

def insert_data():
    cursor.execute('''INSERT INTO secure_data (name, value)
                      VALUES ('Confidential', 'Secret1234')''')
    conn.commit()

def manipulate_data():
    cursor.execute('''UPDATE secure_data
                      SET value = 'CompromisedData'
                      WHERE name = 'Confidential' ''')
    conn.commit()

def fetch_data():
    cursor.execute('SELECT * FROM secure_data')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Create table and insert initial data
create_table()
insert_data()
fetch_data()

# Manipulate data
manipulate_data()
fetch_data()

# Close the connection
conn.close()
