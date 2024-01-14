import sqlite3
dbfile="MBEDB.db"
conn=sqlite3.connect(dbfile)
if conn:
    print("database connetc")

    cursor=conn.cursor()
    cursor.execute("select sqlite_version();")
    vrzn=cursor.fetchone()
    print(vrzn)
else:
    print("fiald connect")

from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)
@app.route("/")
def Index():
    return render_template("Index.html")
@app.route("/testpage")
def test():
   conn = sqlite3.connect('MBEDB.db')
   cursor = conn.cursor()
   cursor.execute("select sum(amount) from expenses;")
   countt=cursor.fetchone()
   conn.close()
   return render_template("testpage.html",value=countt[0])

if __name__=='__main__':
    app.run(debug=True)

