#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("0-index.html")



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=3000, debug=True)


