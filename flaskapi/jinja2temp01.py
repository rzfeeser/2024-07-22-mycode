#!/usr/bin/env python3

# python3 -m pip install flask
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hellobasic.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

