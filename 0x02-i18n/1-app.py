#!/usr/bin/env python3
""" Starts a flask web application """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config():
    """ Configuration setting for flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def render_index_html():
    """ Renders the 1-index.html """
    return render_template('1-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
