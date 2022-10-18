import mysql.connector
import time

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="vijay1234",
    database="testdb"
    )

def create_table(x):
    cursor = mydb.cursor()
    sql = """CREATE TABLE {} (id INT AUTO_INCREMENT PRIMARY KEY,
             email VARCHAR(255), username VARCHAR(255), rollno VARCHAR(255), password VARCHAR(255))""".format(x)
    cursor.execute(sql)

def delete_table(x):
    cursor = mydb.cursor()
    sql = "DROP TABLE {}".format(x)
    cursor.execute(sql)

def insert_user(x, email, username, rollno, password):
    cursor = mydb.cursor()
    add_data = ("INSERT INTO {} (email, username, rollno, password) VALUES (%(a)s, %(b)s, %(c)s, %(d)s)".format(x))
    details = {
    'a':email,
    'b':username,
    'c':rollno,
    'd':password,
    }

    cursor.execute(add_data,details)
    mydb.commit()


def validate(x, username, password):
    cursor = mydb.cursor()
    cursor.execute("select password from {} where username = '{}'".format(x, username))
    if cursor.fetchall()[0][0] == password:
        return 1
    else:
        return 0

