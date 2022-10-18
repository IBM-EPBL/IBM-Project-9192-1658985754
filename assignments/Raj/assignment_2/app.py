from flask import Flask, render_template, request
from flask import redirect, make_response, url_for
from flask import session

from db import insert_user, validate

app = Flask(__name__)

@app.route("/register", methods=['GEt', 'POST'])
def register():

    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        rollno = request.form['rollno']
        password = request.form['password']

        print("Inserting user [ {} - {} - {} - {} ] into database".format(email, username, rollno, password))

        insert_user("user_table", email, username, rollno, password)

        return redirect(url_for('login'))

    return render_template("reg.html")

@app.route("/login", methods=['GEt', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if validate("user_table", username, password) == 1:
            return render_template("index.html")

    return render_template("logpage.html")

@app.route("/main", methods=['GEt', 'POST'])
def welcome():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)