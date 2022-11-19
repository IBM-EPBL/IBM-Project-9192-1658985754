from flask import Flask, render_template,url_for, request,session,redirect
import sqlite3, hashlib 

app = Flask(__name__)
conn = sqlite3.connect('ibm.db')
print("Connection successfull")
app.secret_key = 'IBM'

@app.route('/')
def home_page():
    return render_template('home.html')

#login
@app.route('/validate_login', methods = ['POST'])
def validate_login():
    flag = 0
    if request.method == 'POST':
        #get credentials from user
        username = request.form['username'] 
        password = request.form['password']
        password = hashlib.md5(password.encode())
        password = password.hexdigest()
        print(username + " " + password)
        
        #validation
        flag = 1
        session['type'] = 'admin'
        session['username'] = username
        
        if flag == 1:
            return redirect(url_for('index'))
        else:
            return "Try again"
        
#index
@app.route('/index')
def index():
    return render_template('index.html')

#show
@app.route('/index/show')
def show():
    return render_template('show.html')

#modify
@app.route('/index/modify')
def modify():
    return render_template('modify.html')

#logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('type')
    return redirect(url_for('home_page'))
    
#register
@app.route('/register')
def register_page():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug = True)