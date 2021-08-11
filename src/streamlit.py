import streamlit as st
import numpy as np
import pandas as pd
from connection_sql import db
import requests




################### title 

st.title('Hello, Bcn!')

################### BODY

st.markdown('<style>body{background-color: #000000}</style>', 
unsafe_allow_html=True)

################### POPULATION BY AGE 

result = requests.get("http://localhost:5000/population_by_age").json()

df = pd.DataFrame(
     result,
     columns=['age', 'total'])

st.vega_lite_chart(df, 
{    
    "title": {"text": "Population by Age", "anchor": "middle", "fontSize": 30, "color": ["#6C04A4"]},
    "width": 800,
    "height": 400,
    "mark": {"type": "bar", "color": ["#6C04A4"]},
    "encoding": {
        'x': {"title": "Population", "aggregate": "sum", "scale": {"domain": [0,700000]}, 'field': 'total'},
        'y': {"title": "Age", 'field': 'age'},
     },
     })

#################### POPULATION BY DISTRICT

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


#################### RENTA BY DISTRICT AND MEAN RENTA 

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

#################### WIFI BY DISTRICT

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


#################### ANIMALS BY DISTRICT

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