from flask import Flask
import streamlit as st

app = Flask(__name__)

@app.route('/')
def index():
    return "hey man!!!"
@app.route('/streamlit')
def streamlit():
    st.title("WELCOME TO MSQ PODCAST BOT!!!")
    with st.form('bot form',clear_on_submit = True,border = True):
        name = st.text_input("Enter guest name")
        theme = st.text_area("Theme of the podcast")
        resume = st.file_uploader("Upload the resume of guest")
        linkedin = st.text_input("Give the guests Linkedin profile url")
        youtube = st.text_area("Enter reference yotuube video url")
        submitted = st.form_submit_button("Generate Podcast questions")
if __name__ == "__main__":
    app.run(debug=True)
