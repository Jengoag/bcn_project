import streamlit as st
import graphs
from PIL import Image
import numpy as np
import pandas as pd

################### title 

st.title('Hello, Bcn!')

title_image = Image.open("./img/skyline.png")
st.image(title_image)


st.markdown("Do you want to know ***'Barcelona'***?")
st.markdown("This application is intended to explore the set of data found on the web. It contains basic data for Barcelona, ​​grouped by districts.")


st.write(" Empezamos ")     


###################  SIDEBAR


st.sidebar.title('Choose your Graph')
option=st.sidebar.selectbox('',('Select graph', 'Population by Age','Population by District', 'Rent by Distric', 'Wifi by District', 'Animals by District', 'Areas by District', 'Population 0-14 by District','Parks by District'))

graphs.get_graph_by_option(option)

st.sidebar.title('Comparative Graph')
option=st.sidebar.selectbox(' ',('Select graph', 'Population by Age','Population by District', 'Rent by Distric', 'Wifi by District', 'Animals by District', 'Areas by District', 'Population 0-14 by District','Parks by District'))

graphs.get_graph_by_option(option)

#################### POSTER 

map_data = pd.DataFrame(
    np.random.randn(10, 2) / [20, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

