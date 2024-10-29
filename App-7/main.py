import streamlit as st
import plotly.express as px
from streamlit.proto.Snow_pb2 import Snow

from backend import get_data

st.title("Weather Forecast for the Next Days")
location = st.text_input("Type in the location: ")
days = st.slider("Number of forecast days: ", min_value=1, max_value=5, help="Select the number of days for forecast.")

option = st.selectbox("Select the data to view", ('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} days in {location}")
if location:
    try:
        filtered_content = get_data(location, days)

        if option == 'Temperature':
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_content]
            dates = [dict["dt_txt"] for dict in filtered_content]
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if option == 'Sky':
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"}

            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_content]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)

    except KeyError:
        st.write("Please enter a valid location")