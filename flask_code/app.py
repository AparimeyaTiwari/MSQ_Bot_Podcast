from flask import Flask, render_template, redirect,request
from werkzeug.utils import secure_filename
import os
from ollama_code.resume_parse import resume_parsing
from ollama_code.text_ner import ner_generator
from ollama_code.theme_generation import theme
from ollama_code.yt_search_agent import convert

combined_data = []
app = Flask(__name__)
app.config['UPLOADS_DIRECTORY'] = 'uploads/'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/podcast_question', methods=['POST'])
def podcast_question():
    my_array = []
    guest = request.name
    file = request.files['file'] #files is an array of files, name
    theme_data = request.theme
    youtube = request.yt
    if file:
        file.save(os.path.join(
            app.config['UPLOADS_DIRECTORY'],
            secure_filename(file.filename)
        ))
        resume_parsing(file)
        
        return 'Data submitted sucessfully!!!Please stand by while we generate the podcast questions'
    return redirect('/process')


if __name__ == "__main__":
    app.run(debug=True, port=8000)