import sqlite3

# Open connection to database
conn = sqlite3.connect('test.db')

# Get id number from the user - try inputting 1, 2, %
id = input("Enter a user id: ")

# Create SQL query
qry = "SELECT * FROM USERS WHERE ID LIKE '" + id + "';"
print("\nExecuting:", qry)
print()

# Query data from the table
rows = conn.execute(qry)

# Display results
for row in rows:
    print(row)

conn.close()
