from flask import Flask
from flask import render_template, redirect

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return "Hello, World!"

@app.route("/trainwreck-comic")
@app.route("/trainwreck-comic/<int:page_num>")
def trainwreck_comic(page_num=1):
    
    pages = [
        "../static/pages/1.png",
        "../static/pages/2.png",
    ]
    page_count = len(pages)
    if page_num < 1:
        return redirect("/trainwreck-comic/1")
    if page_num > page_count:
        return redirect(f"/trainwreck-comic/{page_count}")

    return render_template("index.html", page_num=page_num, page_count=page_count, page = pages[page_num - 1])
