from flask import Flask, render_template, redirect,request, send_file
from werkzeug.utils import secure_filename
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from my_package.questions_gen import question_generator
from my_package.resume_parse import resume_parsing
from my_package.text_ner import ner_generator
from my_package.theme_generation import theme
from my_package.yt_search_agent import convert




combined_data = []
app = Flask(__name__)
app.config['UPLOADS_DIRECTORY'] = 'uploads/'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/podcast_question', methods=['POST'])
def podcast_question():
    my_array = []
    guest = request.form['guest_name']
    global name
    name = guest
    imp = request.form['main_topics']
    file = request.files['file'] #files is an array of files, name
    topic = request.form['topics']
    youtube = request.form['yt']
    if file:
        file.save(os.path.join(
            app.config['UPLOADS_DIRECTORY'],
            secure_filename(file.filename)
        ))
        resume_parsing(f'uploads/{file.filename}')
        file_name = os.path.splitext(file.filename)
        final_name = file_name[0]+'.txt'
        ner_generator(f'json/{final_name}',my_array)
        theme(youtube,my_array)
        question = question_generator(my_array,topic,imp)
        convert(question,guest)
        output = os.path.join(os.path.expanduser('~'),'Downloads','MSQ_BOT_PODCAST','flask_code','static',f'{name}.pdf')
        if(os.path.exists(output) == False):
            return "Error questions not generated"
        send_file(
            output,
            as_attachment = True,
            download_name=f'{guest}.pdf'
        )
        return render_template('page2.html',name=name)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, port=8000)