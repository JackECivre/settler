from collections import defaultdict

from flask import Flask, render_template, request
import threading
import time
import requests
from database.sqlite_db import DB

app = Flask(__name__)

DB_FILE = "./database/settler.db"
db = DB(DB_FILE)
conn = db.conn

users = [{
    "id": 1,
    "username": "Pinny",
    "first_name": "Eric",
    "last_name": "Pinhasovich",
    "date_of_birth": "12/08/1991",
    "address": "59 Florentin",
    "current_city": "Tel Aviv",
    "origin_country": "USA"
}]


@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/signup", methods=['GET'])
def sign_up():
    return render_template("signup.html")


@app.route("/welcome", methods=['POST'])
def create_user():
    user = {
    "username": request.form['username'],
    "first_name": request.form['first_name'],
    "last_name": request.form['last_name'],
    "date_of_birth": request.form['bday'],
    "address": request.form['address'],
    "current_city": request.form['city_of_residence'],
    "origin_country": request.form['country_of_origin']
    }

    db = DB(DB_FILE)
    user_data_to_db = list(user.values())
    db.signup_to_db(user_data_to_db)

    return render_template("welcome.html", user=user)


@app.route("/map", methods=['GET'])
def map():
    return render_template("maps.html")


@app.route("/quiz", methods=['GET'])
def quiz():
    return render_template("quiz.html")


@app.route("/quiz/language", methods=['GET'])
def quiz_language():
    return render_template("quizLang.html")


@app.route("/quiz/food", methods=['GET'])
def quiz_food():
    return render_template("quizFood.html")


@app.route("/quiz/pop", methods=['GET'])
def quiz_pop():
    return render_template("quizPop.html")


@app.route("/quiz/rec", methods=['GET'])
def quiz_rec():
    return render_template("quizRec.html")


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
    return render_template("host.html")


@app.route("/meal/host", methods=['POST'])
def create_meal():
    def meal_tags():
        meal_type = []
        for key, val in request.form.items():
            if key.startswith('type'):
                meal_type.append(val)
        return meal_type
    listing = {
        # TODO: Match the data from HTML to the table in DB.
        # problem with: first_name, last_name, date_of_birth, origin_country. need to get it from automatic from connected user.
        # problem with: meal_time, meal_type, current_city, address -> no in social_meals table.
        # big problem: meal preference: it is list. should be one string or create new table for types.
        # "first_name": request.form['first_name'],
        # "last_name": request.form['last_name'],
        # "date_of_birth": request.form['bday'],
        # "origin_country": request.form['country_of_origin'],
        # "address": request.form['address'],
        # "current_city": request.form['city_of_residence'],
        "number_of_guests": request.form['number_of_guests'],
        # "meal_preference": meal_tags(),
        "event_date": request.form['meal_date'],
        # "meal_time": request.form['meal_time']
        "creator_id": 1,  # TODO: Warring: hard code -  should be connected user id
        "meal_preference": "kosher"  # TODO: Warring: hard code - should be from the form.
    }

    db = DB(DB_FILE)
    meal_data = list(listing.values())
    db.host_meal_to_db(meal_data)

    return render_template("listings.html", listing=listing)


@app.route("/meal/listings", methods=['GET'])
def view_meals():
    return render_template("listings.html")


@app.route("/meal/hosted/listing", methods=['GET'])
def listing():
    return render_template("listing.html")


if __name__ == "__main__":
    threading.Thread(target=app.run).start()

response = request.get('http://127.0.0.1:5000')
if response.status_code == 200 and response.text == "Hello":
    print('OK')
else:
    print('Error')