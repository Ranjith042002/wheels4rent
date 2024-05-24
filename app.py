from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app=Flask(__name__)


app.config["MONGO_URI"] = os.getenv('mongo_url')
client=MongoClient(os.getenv('mongo_url'))
db=client['Wheels4rent']

@app.route('/')
def home():
    try:
        return render_template('register.html')
    except:
        return "not working"

@app.route('/register', methods=['GET', 'POST'])
def register_new_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        terms_accepted = 'terms' in request.form

        # Check if the email is already registered
        existing_user = db.users.find_one({'email': email})
        if existing_user:
            return 'Email already exists. Please use a different email.'

        # Insert the new user into the database
        new_user = {'username': username, 'email': email, 'password': password, 'terms_accepted': terms_accepted}
        db.users.insert_one(new_user)

        return render_template('login.html')


    return render_template('register.html')


@app.route('/login', methods=['GET','POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the user exists in the database and password matches
        user = db.users.find_one({'email': email, 'password': password})
        if user:
            return redirect(url_for('ride'))  # Redirect to ride page after successful login
        else:
            return 'Invalid credentials. Please try again.'

    return render_template('login.html')

@app.route('/ride', methods=['GET', 'POST'])
def ride():
    if request.method == 'POST':
        location = request.form.get('location')
        pickup_date = request.form.get('pickup_date')
        pickup_time = request.form.get('pickup_time')
        return_date = request.form.get('return_date')
        return_time = request.form.get('return_time')

        new_ride = {'location': location, 'pickup_date': pickup_date, 'pickup_time': pickup_time,'return_date': return_date, 'return_time': return_time}
        db.ride.insert_one(new_ride)

        return redirect(url_for('services'))

    return render_template('ride.html')



if __name__ =="__main__":
    app.run(debug=True)