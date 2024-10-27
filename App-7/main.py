import streamlit as st

st.title("Weather Forecast for the Next Days")
location = st.text_input("Type in the location: ")
days = st.slider("Number of forecast days: ", min_value=1, max_value=5, help="Select the number of days for forecast.")

option = st.selectbox("Select the data to view", ('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} days in {location}")
