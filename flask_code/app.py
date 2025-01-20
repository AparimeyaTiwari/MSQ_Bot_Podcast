from flask import Flask, Response, render_template, request, url_for,redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<name>")
def user(name):
    return f"HELLO: {name}"

@app.route("/page2",methods = ['POST'])
def second_page():
    html_data = request['resume']
    return render_template("page2.html", html_data = html_data)

@app.route("/admin")
def admin():
    return redirect(url_for("user",name="ADMIN!!"))

if __name__ == "__main__":
    app.run(debug=True)