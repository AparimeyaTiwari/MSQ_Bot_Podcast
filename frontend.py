import streamlit as st # type: ignore
st.title("Welcome to the AI podcast questionnaire maker")
with st.form(key='myf',clear_on_submit=False,enter_to_submit=False,border=True):
    st.text_input(label='Guest Name',placeholder="Enter guest name")
    st.text_area(label="Theme Information",placeholder="Enter topics that you wanna discuss in your podcast")
    st.file_uploader(label='Guest resume')
    st.text_input(label='Youtube Link',placeholder="Enter reference podcast youtube references")
    st.form_submit_button(label="Generate Podcast Questions",type="primary")