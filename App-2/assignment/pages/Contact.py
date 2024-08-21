import streamlit as st
from email_sender import sendEmail

st.header("Fill this form to reach-out to us!")

with st.form(key='form'):
    user_email = st.text_input("Your Email Address")
    topic = st.selectbox(
        "What topic would you like to help with?",
        ("Careers", "Tenders", "Projects", "Others")
    )
    message = st.text_area("Your Message")
    content = f"""\
Subject: Form filled by {user_email}!

From: {user_email}
Topic: {topic}
{message}
"""
    submit_btn = st.form_submit_button('Submit')
    if submit_btn:
        sendEmail(content)
        st.info("Email sent successfully")
