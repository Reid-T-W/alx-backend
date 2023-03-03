#!/usr/bin/env python3
""" Starts a flask web application """
from flask import Flask, render_template, g, request
from flask_babel import Babel, gettext

app = Flask(__name__)


class Config():
    """ Configuration setting for flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Get best suited language according to users preference"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# babel.init_app(app, locale_selector=get_locale)


@app.route('/', strict_slashes=False)
def render_index_html():
    """ Renders the 3-index.html """
    return render_template('3-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
