import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
location = st.text_input("Type in the location: ")
days = st.slider("Number of forecast days: ", min_value=1, max_value=5, help="Select the number of days for forecast.")

option = st.selectbox("Select the data to view", ('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} days in {location}")

def get_data(days):
    dates = ['2024-25-10', '2024-26-10', '2024-27-10', '2024-28-10']
    temperatures = ['10', '11', '10', '13']
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_data(days)
figure = px.line(x=d, y=t, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)