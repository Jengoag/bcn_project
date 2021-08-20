import streamlit as st
import graphs
from PIL import Image
import card

################### title 

st.markdown("<h1 style='text-align: center; color: #942953 '>Hello, BCN!</h1>", unsafe_allow_html = True)

title_image = Image.open("./src/img/skyline.png")
st.image(title_image)


st.markdown("Do you want to know ***'Barcelona'***?")
st.markdown("This application is intended to explore the set of data found on the web. It contains basic data for Barcelona, ​​grouped by districts.")
   

###################  SIDEBAR


st.sidebar.title('Choose your Graph')
option=st.sidebar.selectbox('',('Select graph', 'Population by Age','Population by District', 'Rent by Distric', 'Wifi by District', 'Animals by District', "Dog's Areas by District",'Parks by District'))

graphs.get_graph_by_option(option)

st.sidebar.title('Choose District')
district = st.sidebar.selectbox('  ',('Select district', 'Ciutat Vella', 'Horta-Guinardó', 'Sants-Montjuïc', 'Sarrià-Sant Gervasi', 'Sant Martí', 'Gràcia', 'Eixample', 'Nou Barris', 'Sant Andreu', 'Les Corts'))

card.get_card_by_district(district)

st.sidebar.title('Choose your Map')
map_option=st.sidebar.selectbox('  ',('Select Map', 'Map Parks', "Map Dog's Areas"))

graphs.get_text_by_option(map_option)
graphs.get_map_by_option(map_option)






