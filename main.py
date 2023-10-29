import streamlit as st
import plotly.express as pt
from backend import get_data

# add title, text input,slider,selectbox nd header
page_bg_img = '''
<style>
body {
background-image: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Fdribbble.com%2Fshots%2F3333720-Weather-App-Background-Image-Free&psig=AOvVaw1K7N3dGzjjWT2fuM6G5JNl&ust=1698699315193000&source=images&cd=vfe&ved=0CBIQjRxqFwoTCJDksZ-SnIIDFQAAAAAdAAAAABAE");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

st.header("Hello everyone")
st.header("Weather forecast for next five days")

place = st.text_input("Enter the city:")
days = st.slider("Forecast days", min_value=1, max_value=5, help="select the days")
option = st.selectbox("Select the data to view", ("temperature", "sky"))
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
