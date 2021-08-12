import pandas as pd
import requests
import streamlit as st


def population_by_age():
    result = requests.get("http://localhost:5000/population_by_age").json()

    df = pd.DataFrame(
         result,
        columns=['age', 'total'])

    st.vega_lite_chart(df, 
{
  "layer": [
    {
        "title": {"text": "Population by Age", "anchor": "middle", "fontSize": 30, "color": ["#9C09A4"]},
        "width": 800,
        "height": 600,
        "mark": "bar",
        "encoding": {
            'y': {"title": "Population", "aggregate": "sum", "scale": {"domain": [0,700000]}, 'field': 'total'},
            'x': {"title": "Age", 'field': 'age'}
        }
      },
    {
        "mark": "rule",
        "encoding": {
         "y": {"aggregate": "mean", "field": "age"},
            "color": {"value": "red"},
            "size": {"value": 3}
      }
    }
  ]
})

def population_by_district():
    result = requests.get("http://localhost:5000/population_by_district").json()

    df = pd.DataFrame(
        result,
        columns=['TOTAL_POPULATION_BY_DISTRICT', 'district'])

    st.vega_lite_chart(df, 
    {    
        "title": {"text": "Population by District", "anchor": "middle", "fontSize": 30, "color": ["#9C09A4"]},
        "width": 800,
        "height": 400,
        "mark": {"type": "bar", "color": ["#9C09A4"]},
        "encoding": {
            'x': {"title": "POPULATION", "aggregate": "sum", "scale": {"domain": [0,1_400_000]}, 'field': 'TOTAL_POPULATION_BY_DISTRICT'},
            'y': {"title": "District", 'field': 'district'},
        },
        })

def renta_by_district():
    result = requests.get("http://localhost:5000/renta_by_district").json()

    df = pd.DataFrame(
        result,
        columns=['import_anual', 'district'])

    st.vega_lite_chart(df, 
    {    
        "title": {"text": "Rent by District", "anchor": "middle", "fontSize": 30, "color": ["#4C08A4"]},
        "width": 1000,
        "height": 400,
        "layer": [
            {
            "mark": {"type": "bar", "color": ["#4C09A4"]},
            "encoding": {
                'x': {"title": "Anual Rent", "aggregate": "sum", "scale": {"domain": [0,33_000]}, 'field': 'import_anual'},
                'y': {"title": "District", 'field': 'district'}
                }
            }, 
            {
            "mark": "rule",
            "encoding": {
                "x": {"aggregate": "mean", "field": "import_anual", "type": "quantitative"},
                "color": {"value": "#FFC300"},
                "size": {"value": 3}
            }
            }
        ]
    })

def wifi_by_district():
    result = requests.get("http://localhost:5000/wifi_by_district").json()

    df = pd.DataFrame(
        result,
        columns=['TOTAL_WIFI_BY_DISTRICT', 'district'])

    st.vega_lite_chart(df, 
    {    
        "title": {"text": "Wifi by District", "anchor": "middle", "fontSize": 30, "color": ["#FFC300"]},
        "width": 800,
        "height": 400,
        "mark": {"type": "bar", "color": ["#FFC300"]},
        "encoding": {
            'x': {"title": "WIFI", "aggregate": "sum", "scale": {"domain": [0, 300]}, 'field': 'TOTAL_WIFI_BY_DISTRICT'},
            'y': {"title": "District", 'field': 'district'},
        },
        })


def animals_by_district():
    result = requests.get("http://localhost:5000/animals_by_district").json()

    df = pd.DataFrame(
        result,
        columns=['total', 'district'])

    st.vega_lite_chart(df, 
    {    
        "title": {"text": "Animals by District", "anchor": "middle", "fontSize": 30, "color": ["#FFC300"]},
        "width": 800,
        "height": 400,
        "mark": {"type": "bar", "color": ["#FFC300"]},
        "encoding": {
            'x': {"title": "Animals", "aggregate": "sum", "scale": {"domain": [0, 10_000]}, 'field': 'total'},
            'y': {"title": "District", 'field': 'district'},
        },
        })
def area_by_district():
    result = requests.get("http://localhost:5000/area_by_district").json()

    df = pd.DataFrame(
        result,
        columns=["TOTAL_AREA_BY_DISTRICT", 'district'])

    st.vega_lite_chart(df, 
    {    
        "title": {"text": "Areas by District", "anchor": "middle", "fontSize": 30, "color": ["#FFC300"]},
        "width": 800,
        "height": 400,
        "mark": {"type": "bar", "color": ["#FFC300"]},
        "encoding": {
            'x': {"title": "Areas", "aggregate": "sum", "scale": {"domain": [0, 20]}, 'field': "TOTAL_AREA_BY_DISTRICT"},
            'y': {"title": "District", 'field': 'district'},
        },
        })

def population_0_14_by_district():
    result = requests.get("http://localhost:5000/population_0_14_by_district").json()

    df = pd.DataFrame(
        result,
        columns=["population_0_14", 'district'])

    st.vega_lite_chart(df, 
    {    
        "title": {"text": "Population 0-14 by District", "anchor": "middle", "fontSize": 30, "color": ["#FFC300"]},
        "width": 800,
        "height": 400,
        "mark": {"type": "bar", "color": ["#FFC300"]},
        "encoding": {
            'x': {"title": "Population", "aggregate": "sum", "scale": {"domain": [0, 105000]}, 'field': "population_0_14"},
            'y': {"title": "District", 'field': 'district'},
        },
        })

def parques_by_district():
    result = requests.get("http://localhost:5000/parques_by_district").json()

    df = pd.DataFrame(
        result,
        columns=['TOTAL_PARQUES_BY_DISTRICT', 'district'])

    st.vega_lite_chart(df, 
    {    
        "title": {"text": "Parks by District", "anchor": "middle", "fontSize": 30, "color": ["#FFC300"]},
        "width": 800,
        "height": 400,
        "mark": {"type": "bar", "color": ["#FFC300"]},
        "encoding": {
            'x': {"title": "Parks", "aggregate": "sum", "scale": {"domain": [0, 120]}, 'field': 'TOTAL_PARQUES_BY_DISTRICT'},
            'y': {"title": "District", 'field': 'district'},
        },
        })




def get_graph_by_option(option):

    if option=='Population by Age':
        population_by_age()

    if option=='Population by District':
        population_by_district()

    if option=='Rent by Distric':
        renta_by_district()

    if option=='Wifi by District':
        wifi_by_district()

    if option=='Animals by District':
        animals_by_district()

    if option=='Areas by District':
        area_by_district()

    if option=='Population 0-14 by District':
        population_0_14_by_district()

    if option=='Parks by District':
        parques_by_district()
    
