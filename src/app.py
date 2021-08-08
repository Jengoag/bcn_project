from flask import Flask
from connection_sql import db
from utils.json_response import json_response

app = Flask("app")

@app.route("/")
def hello_world():
    return "<p>Hello, BCN!</p>"

@app.route("/animals")
def search_animals():
    query = f"""
        SELECT * FROM animals;
    """
    result = db.execute(query).fetchall()

    return json_response(result)

@app.route("/total_population")
def search_total_population():
    query = f"""
        SELECT population FROM population;
    """
    result = db.execute(query).fetchall()

    return json_response(result)

@app.route("/population_district_total")
def search_population_district_total():
    query = f"""
        SELECT district, total FROM population;
    """
    result = db.execute(query).fetchall()

    return json_response(result)
