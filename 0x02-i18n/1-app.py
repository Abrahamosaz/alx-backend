#!/usr/bin/env python3
from flask import Flask
from flask_babel import Babel

class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)

