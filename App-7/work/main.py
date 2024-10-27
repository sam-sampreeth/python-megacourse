import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In search for happiness")
xax = st.selectbox("Select data for x-axis: ", ('GDP', 'Happiness', 'Generosity'))
yax = st.selectbox("Select data for y-axis: ", ('GDP', 'Happiness', 'Generosity'))

df = pd.read_csv('happy.csv')
match xax:
    case "Happiness":
        x_arr = df['happiness']
    case "Generosity":
        x_arr = df['generosity']
    case "GDP":
        x_arr = df['gdp']

match yax:
    case "Happiness":
        y_arr = df['happiness']
    case "Generosity":
        y_arr = df['generosity']
    case "GDP":
        y_arr = df['gdp']


st.subheader(f"{xax} and {yax}")
fig1 = px.scatter(x=x_arr, y=y_arr, labels={"x": xax, "y": yax})
st.plotly_chart(fig1)
