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

## MEAN RENTA ######### NO NECESARIA, STREAMLIT TIENE SU PROPIA FUNCION 

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


## WIFI - RENTA BY DISTRICT  ######### SIN HACER 

@app.route("/wifi_renta_by_district")
def search_wifi_renta_by_district():
    query = f"""
        SELECT renta.district, renta.import_anual,
        count(wifi.district) as TOTAL_WIFI_BY_DISTRICT
        FROM renta, wifi
        WHERE renta.district = wifi.district
        GROUP BY renta.district, renta.import_anual, wifi.district
    ;  
 
    """
    result = db.execute(query).fetchall()

    return json_response(result)

## POPULATION - RENTA BY DISTRICT ############ SIN HACER 

@app.route("/population_renta_by_district")
def search_population_renta_by_district():
    query = f"""
        SELECT renta.district, renta.import_anual,
        sum(population.total) as TOTAL_POPULATION_BY_DISTRICT
        FROM renta, population
        WHERE renta.district = population.district
        GROUP BY renta.district, renta.import_anual, population.district
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

# ANIMALS AND AREAS BY DISTRICT

@app.route("/animals_and_areas_by_district")
def search_animals_and_areas_by_district():
    query = f"""
        SELECT animals.district, animals.total as total_animals,
        COUNT(areaperros.district) AS TOTAL_AREA_BY_DISTRICT
        FROM animals, areaperros
        WHERE animals.district = areaperros.district
        GROUP BY animals.district, animals.total, areaperros.district
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)

# POPULATION 0-15 BY DISTRICT

@app.route("/population_0_14_by_district")
def search_population_0_14_by_district():
    query = f"""
        SELECT district, SUM(total) FROM population
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
        COUNT(district) AS TOTAL_PARQUES_BY_DISTRICT
        FROM parques 
        group BY district
        ;
    """
    result = db.execute(query).fetchall()

    return json_response(result)


# POPULATION 0-14 AND PARQUES BY DISTRICT (NO FUNCIONA )

@app.route("/population_0_14_and_parques_by_district")
def search_population_0_14_and_parques_by_district():
    query = f"""
        SELECT parques.district,
        COUNT(parques.district) AS TOTAL_PARQUES_BY_DISTRICT,
        population.district, SUM(population.total) as TOTAL_POPULATION_0_14_BY_DISTRICT FROM population
        WHERE age LIKE '0-4' or AGE LIKE '5-9'or AGE LIKE '10-14'
        GROUP BY DISTRICT
        ORDER BY DISTRICT
        FROM parques, population
        WHERE parques.district = population.district
        GROUP BY parques.district, parques.total_parques_by_district, population.district, population.TOTAL_POPULATION_0_14_BY_DISTRICT
        ;
    """
    result = db.execute(query).fetchall()

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






