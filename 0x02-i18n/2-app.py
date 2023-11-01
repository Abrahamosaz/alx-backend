#!/usr/bin/env python3
"""Flask Application"""
from flask_babel import Babel
from flask import Flask, request
from flask import render_template

class Config(object):
    """Class Configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    
app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)



@app.route('/', strict_slashes=False)
def index():
    """Index of a file"""
    return render_template('2-index.html')

@babel.localeselector
def get_locale():
    """Gets the locale selector"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == "__main__":
    app.run(port='5000', host='0.0.0.0', debug=True)