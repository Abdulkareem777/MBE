import sqlite3

# Replace 'your_database_name.db' with the name of your SQLite database file
db_file = 'MBEDB.db'

# Create a connection
conn = sqlite3.connect(db_file)

# Check if the connection is successful
if conn:
    print("Connected to SQLite database")

    # Now you can perform operations like creating a cursor and executing queries
    cursor = conn.cursor()

    # For example, execute a simple query
    cursor.execute("SELECT sqlite_version();")
    version = cursor.fetchone()
    print(f"SQLite version: {version[0]}")

    # Close the cursor and connection when done
    cursor.close()
    conn.close()
else:
    print("Connection to SQLite database failed")
