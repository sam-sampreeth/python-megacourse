import streamlit as st
import plotly.express as px
import sqlite3

connection = sqlite3.connect("data1.db")
cursor = connection.cursor()
cursor.execute("Select date from temps")
date = cursor.fetchall()
date = [item[0] for item in date]

cursor.execute("Select temp from temps")
temperature = cursor.fetchall()
temperature = [item[0] for item in temperature]

figr = px.line(x=date, y=temperature, labels={"x": "Date", "y": "Temperature"})

st.plotly_chart(figr)