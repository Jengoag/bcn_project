from flask import Flask
from connection_sql import db
from utils.json_response import json_response

app = Flask("app")

@app.route("/")
def hello_world():
    return "<p>Hello, BCN!</p>"


## POPULATION BY AGE 

@app.route("/population_by_age")
def search_population_by_age():
    query = f"""
        SELECT age, total 
        FROM population
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)

## POPULATION BY DISTRICT

@app.route("/population_by_district")
def search_population_by_district():
    query = f"""
        SELECT DISTRICT,
        SUM(total) AS "TOTAL_POPULATION_BY_DISTRICT"
        FROM POPULATION 
        group BY district
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)

## RENTA BY DISTRICT

@app.route("/renta_by_district")
def search_renta_by_district():
    query = f"""
        SELECT district, import_anual 
        FROM renta
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)

## MEAN RENTA 

@app.route("/mean_renta")
def search_mean_renta():
    query = f"""
        SELECT AVG(import_anual) 
        FROM renta
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)


## WIFI BY DISTRICT

@app.route("/wifi_by_district")
def wifi_by_district():
    query = f"""
        SELECT DISTRICT,
        COUNT(district) AS "TOTAL_BY_DISTRICT"
        FROM wifi 
        group BY district
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)






