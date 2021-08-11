import streamlit as st
import numpy as np
import pandas as pd
from connection_sql import db
import requests

st.title('Hello, Bcn!')

###################
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
        'x': {"title": "Population", "aggregate": "sum", "scale": {"domain": [0,800000]}, 'field': 'total'},
        'y': {"title": "Age", 'field': 'age'},
     },
     })
####################




st.title('POPULATION')
query = f"""
    SELECT * FROM population;
    """

result = db.execute(query).fetchall()

df = pd.DataFrame(
     result,
     columns=['code_district', 'district', 'total'])

st.vega_lite_chart(df, {
    "height": {"step": 17},
     'mark': {'type': 'bar' },
     'encoding': {
         'x': {"aggregate": "sum", 'field': 'total' },
         'y': {'field': 'district'},
     },
     })

