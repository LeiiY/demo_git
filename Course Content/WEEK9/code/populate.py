import sqlite3

# Open connection to database. Create the database file if it doesn't exist
conn = sqlite3.connect('test.db')

# Populate the table with a couple of records
conn.execute('''INSERT INTO USERS (ID, NAME, AGE, ADDRESS) VALUES
        (1, 'Fred Bloggs', 21, '12, High Street'),
        (2, 'Susan Smith', 14, '128, Longton Road');''')

# Commit the changes
conn.commit()

conn.close()
