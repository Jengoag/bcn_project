# Hello, Bcn!

![](./src/img/skyline_liner.jpeg)



### DATABASE


- [Kaggle Dataset](https://www.kaggle.com/xvivancos/barcelona-data-sets)
- [Open Data Barcelona Dog's Areas](https://opendata-ajuntament.barcelona.cat/data/es/dataset/arees-esbarjo-gossos-bcn)
- [Open Data Barcelona Parks](https://opendata-ajuntament.barcelona.cat/data/es/dataset/culturailleure-espaisinfantils)
- [Open Data Animals](https://opendata-ajuntament.barcelona.cat/data/es/dataset/cens-animals-companyia)
- [Open Data Wifi](https://opendata-ajuntament.barcelona.cat/data/es/dataset/punts-wifi)
- [Open Data Renta](https://opendata-ajuntament.barcelona.cat/data/es/dataset/renda-disponible-llars-bcn)


###  POSTGRES - DATA 

<img src="./src/img/postgresimg.png" width="50" height="50">

- The data set that has been collected from the web, was in CSV format.

- This data has been cleaned in Jupyter Nootebook and subsequently imported to Postgress.

- In the `data` folder of this project, you can find all the original CSVs and their respective equivalents already cleaned

- In the `code` folder of this project, you can find all the Jupyter Notebook files where the data has been cleaned up..

#### Data Folder

These are the files used. 

- `animalscleaned`
- `areaperros_celaned`
- `parques_cleaned` 
- `population_cleaned` 
- `renta_cleaned` 
- `wifi_cleaned` 

(Remember that in addition, in this folder are the files without cleaning)


#### Code Folder

These are the Jupyter NotebooK files, in which the data is cleaned. Later the tables are created in postgres and the data is imported.

- `animalscode`
- `areaperroscode`
- `parquescode` 
- `populationcode` 
- `rentacode` 
- `wificode` 


### FLASK - API

<img src="./src/img/flaskimg.png" width="75" height="75">

For this project we have used Flask to create our API. This will be the one that makes the calls to the database.

The files needed to start our Api with flask are in the `src` folder, they are the following:

- `json_response.py`- (inside the folder utils)
- `connection_sql.py`
- `app.py` - All requests made to the database


### STREAMLIT

<img src="./src/img/streamlitimg.png" width="75" height="75">

With streamlit we will be able to visualize the data in our browser.

For this, all the files are in the `src` folder, these are:


- `streamlite.py` - All requests made to API.
- `graphs.py` - All graphs and maps.
- `target.py` - All data cards pre-collected by district.


### TOOLS

<img src="./src/img/opendataimg.png" width="200" height="50">
<img src="./src/img/jupyterimg.jpeg" width="150" height="100">
<img src="./src/img/postgresimg.png" width="100" height="100">
<img src="./src/img/flaskimg.png" width="100" height="100">
<img src="./src/img/streamlitimg.png" width="100" height="100">

### CREDITS 

<img src="./src/img/corecodeimg.jpeg" width="50" height="50">

Poject for Bootcamp  ***"Big Data and Machine Learning Bootcamp"*** in en [Core Code School](https://www.corecode.school/)

