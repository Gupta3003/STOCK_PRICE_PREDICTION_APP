from flask_mysqldb import MySQL

mysql = MySQL()

def initDb(app):
    mysql = MySQL(app)