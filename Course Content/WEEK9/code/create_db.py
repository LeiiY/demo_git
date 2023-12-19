import sqlite3

# Open connection to database. Create the database file if it doesn't exist
conn = sqlite3.connect('test.db')

# Delete table 'USERS'. Exception will be thrown if table doesn't exist
try:
    conn.execute('''DROP TABLE USERS;''')
except:
    pass

# Create a table
conn.execute('''CREATE TABLE USERS
         (ID  INT,
         NAME TEXT,
         AGE INT,
         ADDRESS TEXT);''')

conn.close()
