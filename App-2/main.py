import streamlit as st


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.png")
with col2:
    st.title("Sampreeth S M")
    content = """
    Passionate 3rd Year CSE Student with a Keen Interest in Technology | Focused on Becoming a Proficient Full-Stack Developer.
    """
    st.info(content)
st.write("Below you can find some of the projectsI have built or collaborated. Please feel free to contact me!")