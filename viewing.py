import sqlite3

# Connect to the SQLite database (replace 'your_database.db' with the actual database file)
conn = sqlite3.connect('python.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute a SELECT query to retrieve data from the bus_booking table
cursor.execute("SELECT * FROM payment_data")

# Fetch all the rows from the result set
rows = cursor.fetchall()

# Display the retrieved data
for row in rows:
    print("ID:", row[0])
    print("Bus Type:", row[1])
    print("Timings:", row[2])
    print("Date:", row[3])
    print("Driver Needed:", row[4])
    print("Pickup Location:", row[5])
    print("Drop Location:", row[6])
    print("\n")

# Close the cursor and the connection
cursor.close()
conn.close()
