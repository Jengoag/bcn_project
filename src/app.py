from flask import Flask
from connection_sql import db
from utils.json_response import json_response

app = Flask("app")

@app.route("/")
def hello():
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

## WIFI BY DISTRICT

@app.route("/wifi_by_district")
def search_wifi_by_district():
    query = f"""
        SELECT DISTRICT,
        COUNT(district) AS "TOTAL_WIFI_BY_DISTRICT"
        FROM wifi 
        group BY district
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)

## ANIMALS BY DISTRICT

@app.route("/animals_by_district")
def search_animals_by_district():
    query = f"""
        SELECT district, total 
        FROM animals
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)


## AREA BY DISTRICT

@app.route("/area_by_district")
def search_area_by_district():
    query = f"""
        SELECT DISTRICT,
        COUNT(district) AS "TOTAL_AREA_BY_DISTRICT"
        FROM areaperros 
        group BY district
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)

# POPULATION 0-15 BY DISTRICT

@app.route("/population_0_14_by_district")
def search_population_0_14_by_district():
    query = f"""
        SELECT district, SUM(total) as population_0_14 FROM population
        WHERE age LIKE '0-4' or AGE LIKE '5-9'or AGE LIKE '10-14'
        GROUP BY DISTRICT
        ORDER BY DISTRICT
    """
    result = db.execute(query).fetchall()

    return json_response(result)

# PARQUES BY DISTRICT

@app.route("/parques_by_district")
def search_parques_by_district():
    query = f"""
        SELECT DISTRICT,
        COUNT(district) AS "TOTAL_PARQUES_BY_DISTRICT"
        FROM parques 
        group BY district
        ;
    """
    result = db.execute(query).fetchall()

    print(result)

    return json_response(result)

# LATITUD LONGITUD PARQUES

@app.route("/xy_parques")
def xy_parques():
    query = f"""
        SELECT name_area, latitude, longitude
        FROM parques
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)

# LATITUD LONGITUD AREAS 

@app.route("/xy_area")
def xy_area():
    query = f"""
        SELECT name_area, latitude, longitude
        FROM areaperros
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)









