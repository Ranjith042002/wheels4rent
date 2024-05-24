from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app=Flask(__name__)

try:
    app.config["MONGO_URI"] = os.getenv('mongo_url')
    client=MongoClient(os.getenv('mongo_url'))
    db=client['Wheels4rent']
except:
    pass

@app.route('/')
def home():
    try:
        return render_template('register.html')
    except:
        return "not working"

if __name__ =="__main__":
    app.run(debug=True)