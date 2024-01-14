
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

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('add_data.html')
@app.route('/back')
def back():
    return render_template('add_data.html')
@app.route('/display')
def display_data():
    conn = sqlite3.connect('MBEDB.db')
    cursor = conn.cursor()
    
    # Fetch data from the 'expenses' table
    cursor.execute("SELECT date, description, amount, category FROM expenses")
    data = cursor.fetchall()
    
    conn.close()

    # Render the display_data.html template with fetched data
    return render_template('view_data.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        date_value = request.form['date']
        description_value = request.form['description']
        amount_value = request.form['amount']
        category_value = request.form['category']

        conn = sqlite3.connect('MBEDB.db')
        cursor = conn.cursor()

        cursor.execute("INSERT  INTO expenses (date, description, amount, category) VALUES (?, ?, ?, ?)",
                       (date_value, description_value, amount_value, category_value))
        conn.commit()
        conn.close()

        return 'Data added successfully'

if __name__ == '__main__':
     app.run(debug=True)

