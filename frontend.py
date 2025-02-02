import streamlit as st # type: ignore
st.title("WELCOME TO MSQ PODCAST BOT!!!")
with st.form('bot form',border = True):
    name = st.text_input("Enter guest name")
    theme = st.text_area("Theme of the podcast")
    resume = st.file_uploader("Upload the resume of guest")
    youtube = st.text_area("Enter reference youtube video url")
    submitted = st.form_submit_button("Generate Podcast questions")