import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from connection_sql import db

st.title('ANIMALS')
query = f"""
    SELECT * FROM animals;
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

