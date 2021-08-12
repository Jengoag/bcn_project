import streamlit as st
import graphs
################### title 

st.title('Hello, Bcn!')

###################  SIDEBAR


st.sidebar.title('Choose your Graph')
option=st.sidebar.selectbox('',('Select graph', 'Population by Age','Population by District', 'Rent by Distric', 'Wifi by District', 'Animals by District', 'Areas by District', 'Population 0-14 by District','Parks by District','Areas and Animals by District'))

graphs.get_graph_by_option(option)

st.sidebar.title('Comparative Graph')
option=st.sidebar.selectbox(' ',('Select graph', 'Population by Age','Population by District', 'Rent by Distric', 'Wifi by District', 'Animals by District', 'Areas by District', 'Population 0-14 by District','Parks by District','Parks by District','Areas and Animals by District'))

graphs.get_graph_by_option(option)