import streamlit as st
from streamlit import button

from email_sender import sendEmail

st.header("Contact us!")

with st.form(key='email_form'):
    user_email = st.text_input("Your Email Address")
    message = st.text_area("Your Message")
    emailContent = f"""\
Subject: Your contact form was filled by {user_email}

From: {user_email}
{message}
"""
    submit_button = st.form_submit_button('Submit')
    if submit_button:
        print("Form was submitted")
        sendEmail(emailContent)
        st.info("Email sent successfully")