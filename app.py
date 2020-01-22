from flask import Flask, render_template
import threading
import time
import requests
from database.db import DB

app = Flask(__name__)

DB_FILE = "./database/settler.db"
db = DB(DB_FILE)
conn = db.conn

@app.route("/")
def hello():
    return "Hello"


@app.route("/signup", methods=['GET'])
def sign_up():
    data = ["avi326", "avi", "barazani", None, "add", "asd", "asd"]
    db = DB(DB_FILE)
    db.signup_to_db(data)
    return render_template("signup.html")


@app.route("/welcome", methods=['GET'])
def welcome():
    return render_template("welcome.html")


@app.route("/map", methods=['GET'])
def map():
    return render_template("maps.html")


@app.route("/prices", methods=['GET'])
def prices():
    return render_template("prices.html")


@app.route("/apps", methods=['GET'])
def apps():
    return render_template("apps.html")


@app.route("/meal", methods=['GET'])
def meal():
    return render_template("meal.html")


@app.route("/meal/createmeal", methods=['GET'])
def host():
    return render_template("createmeal.html")


@app.route("/meal/hosted", methods=['GET'])
def hosted():
    return render_template("hosted.html")


@app.route("/meal/hosted/listing", methods=['GET'])
def listing():
    return render_template("listing.html")


if __name__ == "__main__":
    threading.Thread(target=app.run).start()

response = requests.get('http://127.0.0.1:5000')
if response.status_code == 200 and response.text == "Hello":
    print('OK')
else:
    print('Error')