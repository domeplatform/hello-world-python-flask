import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world! This Python Flask app is brought to you by Dome Global"

if __name__ == "__main__":
    app.run()

def run():
    port = int(os.getenv("PORT"))
    app.run(host='0.0.0.0', port=port)
