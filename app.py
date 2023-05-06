from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world! This Python Flask app is brought to you by Dome Global"