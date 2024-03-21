import sqlite3

# Connect to the SQLite database (replace 'your_database.db' with the actual database file)
conn = sqlite3.connect('bus_reservation.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SELECT query to retrieve data from the bus_data table

cursor.execute("SELECT * FROM bus_data")

# Fetch all the rows from the result set
rows = cursor.fetchall()

# Display the retrieved data
for row in rows:
    print("ID:", row[0])
    print("From Location:", row[1])
    print("To Location:", row[2])
    print("Date:", row[3])
    
    print("\n")

# Close the cursor and the connection
cursor.close()
conn.close()
