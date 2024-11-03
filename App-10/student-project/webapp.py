import streamlit as st
import plotly.express as px
import pandas

df = pandas.read_csv('data1.txt')

fgr = px.line(x=df["date"], y=df[" temperature"], labels={"x": "date", "y": "temperature"})

st.plotly_chart(fgr)