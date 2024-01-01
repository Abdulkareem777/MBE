from flask import Flask, render_template
import sqlite3

app = Flask(__name__)
@app.route('/back')
def index():
    return render_template('add_data.html')
@app.route('/display')
def display_data():
    conn = sqlite3.connect('MBEDB.db')
    cursor = conn.cursor()
    
    # Fetch data from the expenses table
    cursor.execute("SELECT date, description, amount, category FROM expenses")
    data = cursor.fetchall()
    
    conn.close()

    return render_template('view_data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
