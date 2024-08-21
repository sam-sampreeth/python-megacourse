import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.jpg", width=550)
with col2:
    st.title("Sampreeth S M")
    content = """
    Passionate 3rd Year CSE Student with a Keen Interest in Technology | Focused on Becoming a Proficient Full-Stack Developer.
    
    I've built a solid base in managing databases, and I'm skilled with MySQL and MongoDB. My work with data structures and algorithms in C, has given me the tools to solve tricky computing problems. As a web developer, I'm good at creating full-stack apps using HTML, CSS, JavaScript, Node.js, Express, and React. On top of that, I know Python well and have a basic grasp of object-oriented programming in Java.
    """
    st.info(content)
st.write("Below you can find some of the projectsI have built or collaborated. Please feel free to contact me!")

col3, sep, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source code](https://github.com/sam-sampreeth)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[Source code](https://github.com/sam-sampreeth)")
