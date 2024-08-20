import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header("The Best Company")
about = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet imperdiet ex. Donec imperdiet et tortor et sodales. Aenean in nulla in mi faucibus fringilla sed in sapien. Nulla pretium eu mi id fringilla. Duis nulla massa, tempor interdum nunc et, ornare vulputate massa. Phasellus dapibus rutrum dapibus. Donec facilisis rhoncus lectus, nec dignissim urna porttitor quis. Proin vulputate aliquet ligula, nec suscipit nisl auctor quis. Integer volutpat, ligula a dapibus maximus, mauris eros tempor arcu, et cursus turpis erat non leo. Proin imperdiet condimentum turpis in iaculis. Nam et lacus convallis augue tincidunt laoreet. Duis vulputate elit in.

"""
st.write(about)
st.subheader("Meet our team!")

df = pd.read_csv("data.csv")
col1, col2, col3 = st.columns(3)
with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/"+row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/"+row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images/"+row["image"])

