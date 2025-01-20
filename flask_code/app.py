from flask import Flask, Response, render_template, request, url_for,redirect
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config["UPLOAD_DIRECTORY"] = "uploads/"

@app.route("/", methods=["POST","GET"])
def home():
    return render_template("index.html")


@app.route("/podcast_question", methods=["POST"])
def podcast_question():
    file = request.files['file'] #files is an array of files, name
    if file:
        file.save(os.path.join(
            app.config["UPLOAD_DIRECTORY"],
            secure_filename(file.filename)
        ))
    else:
        return "No file uploaded"
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)