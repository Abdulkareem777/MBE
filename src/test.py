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
