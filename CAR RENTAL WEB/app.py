from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
# from flask_cors import CORS
import os

app = Flask(__name__)
# CORS(app)


@app.route('/')
def home():
    try:
        return render_template('register.html')
    except:
        return "Not Working"

if __name__ =="__main__":
    app.run(debug=True)