from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    template = render_template("index.html")
    return template