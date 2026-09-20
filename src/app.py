from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/trainwreck-comic")
def trainwreck_comic():
    return render_template("index.html")