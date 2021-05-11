#Importing all necessary libraries 
import pandas as pd 
import plotly.express as px
import gzip, pickle
import streamlit as st

#loading of non-compressized pickle file 
#pickle_in = open('model.pkl', 'rb') 
#classifier = pickle.load(pickle_in)

#deserialize/loading of pickle file (compressized)
filepath = "time.pkl"
with gzip.open(filepath, 'rb') as f:
    p = pickle.Unpickler(f)
    classifier= p.load()


#Load the row & clean dataset
rawdata = pd.read_excel("Raw_Delhi.xlsx")
cleaneddata = pd.read_csv("delhi_AQIclean.csv",index_col=0)



#Create the Main title of web page 
st.title("DELHI AQI FORECASTING")




#create the color background & subtitle 
html_temp = """
<div style="background-color:tomato;padding:9px">
<h1 style="color:white;text-align:center;">PM2.5 Value Prediction </h>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)

page_bg_img = '''
<style>
body {
background-image: url("https://d3i6fh83elv35t.cloudfront.net/newshour/app/uploads/2016/11/RTX2R4NJ.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

#Create the nevigator or sidebar

nav = st.sidebar.radio("Navigation",["None","Raw Data","Cleaned Data","Prediction"])


#Create condition according desired output
if nav == "None":
    st.write("Welcome To Delhi AQI Future PM2.5 Value Prediction with Stremlit")
#Printing time series plot and dataframe for Raw data 
if nav == "Raw Data":
    
    if st.checkbox("Show Raw Data"):
        st.dataframe(rawdata, width = 500 , height = 200 )
    
    graph = st.selectbox("What kind of Graph ? ",["None","Time Series Plot"])

    if graph == "None":
       st.write() 
    
    if graph == "Time Series Plot":
       
        
        fig = px.line(rawdata, x = 'date', y = 'pm25', title = 'PM2.5 Value On Monthly With Slider', width = 800)

        fig.update_xaxes(
            rangeslider_visible = True,
            rangeselector = dict(
                buttons = list([
                    dict(count=1, label= "1m", step="month", stepmode= "backward"),
                    dict(count=2, label= "2m", step="month", stepmode= "backward"),
                    dict(count=3, label= "3m", step="month", stepmode= "backward"),
                    dict(count=4, label= "4m", step="month", stepmode= "backward"),
                    dict(step= "all")
                ])
            )
        )
        st.plotly_chart(fig)
       
    
#Printing time series plot and dataframe for clean data      
if nav == "Cleaned Data":
    
    if st.checkbox("Show Cleaned Data"):
        st.dataframe(cleaneddata, width = 500 , height = 200 )
    
    graph = st.selectbox("What kind of Graph ? ",["None","Time Series Plot"])

    if graph == "None":
       st.write() 
    
    if graph == "Time Series Plot":
       
        
        fig = px.line(cleaneddata, x = cleaneddata.index , y = 'pm25', title = 'PM2.5 Value On Monthly With Slider', width = 800)

        fig.update_xaxes(
            rangeslider_visible = True,
            rangeselector = dict(
                buttons = list([
                    dict(count=1, label= "1m", step="month", stepmode= "backward"),
                    dict(count=2, label= "2m", step="month", stepmode= "backward"),
                    dict(count=3, label= "3m", step="month", stepmode= "backward"),
                    dict(count=4, label= "4m", step="month", stepmode= "backward"),
                    dict(step= "all")
                ])
            )
        )
        st.plotly_chart(fig)
#Printing dataframe for predicted output 
if nav == "Prediction":
    st.header("Know Predicted PM2.5 Value")
    val = st.number_input('How many hours forecast do you want?', min_value = 1, max_value = 24)
    prediction = classifier.forecast(val)
    if st.button("Predict"):
        #st.success(f"Your predicted PM2.5 value is {round(prediction)}") 
        st.dataframe(round(prediction), width = 500 , height = 200 )
        
     
        
        
        
        
        
        
        