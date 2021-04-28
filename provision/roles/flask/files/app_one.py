# -------------------------------------------------
#
# Flask app that serves two simple routes
#
# -------------------------------------------------

from flask import Flask
from flaskext.mysql import MySQL
app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'app_one_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'bimb0'
app.config['MYSQL_DATABASE_DB'] = 'app_one_db'
app.config['MYSQL_DATABASE_HOST'] = '10.0.26.111'
mysql.init_app(app)

conn = mysql.connect()

cursor = conn.cursor()

@app.route("/")
def main():
    return "Welcome to the demo flask app!"

@app.route('/xyz')
def xyz():
    return 'This is the first route to path /xyz'

@app.route('/pqrs')
def pqrs():
    return 'This is the second route to path /pqrs'

@app.route('/read from database')
def read():
    cursor.execute("SELECT * FROM app_one_db")
    row = cursor.fetchone()
    result = []
    while row is not None:
      result.append(row[0])
      row = cursor.fetchone()

    return ",".join(result)

if __name__ == "__main__":
    app.run()
