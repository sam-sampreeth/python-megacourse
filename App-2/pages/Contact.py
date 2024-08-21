import streamlit as st
from streamlit import button

st.header("Contact us!")

with st.form(key='email_form'):
    user_email = st.text_input("Your Email Address")
    message = st.text_area("Your Message")
    submit_button = st.form_submit_button('Submit')
    if submit_button:
        print("Form was submitted")