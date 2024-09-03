from .app import app, data
from flask import render_template

@app.route('/')
def home():
    return render_template(
        "home.html", title="Hello World", names=["Jean","Paul","Louis"]
    )

@app.route('/books')
def page_livre():
    return render_template(
        "book.html", data=data
    )   