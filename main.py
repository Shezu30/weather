import streamlit as st
import plotly.express as pt
from backend import get_data

# add title, text input,slider,selectbox nd header
st.header("Weather forecast for next five days")

place = st.text_input("enter the city")
days = st.slider("forecast days", min_value=1, max_value=5, help="select the days")
option = st.selectbox("select the data to view", ("temperature", "sky"))
st.subheader(f"{option} for next {days} days in {place}")
if place:
    filtered_data = get_data(place, days)

    if option == "temperature":
        t = [dict["main"]["temp"] for dict in filtered_data]
        d = [dict["dt_txt"] for dict in filtered_data]
        # graph figure with timeline
        figure = pt.line(x=d, y=t, labels={"x": "date", "y": "temperature (C)"})
        st.plotly_chart(figure)

    if option == "sky":
        images = {"Clear": "images/clear.png",
                  "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}

        sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
        image_path = [images[condition] for condition in sky_condition]
        st.image(image_path, width=115)
