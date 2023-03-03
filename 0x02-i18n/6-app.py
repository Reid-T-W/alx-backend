#!/usr/bin/env python3
""" Starts a flask web application """
from flask import Flask, render_template, g, request
from flask_babel import Babel, gettext
from flask_babel import _

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
    # Checking if lang is specified in url (1st priority)
    lang = request.args.get('locale')
    if lang is not None and lang in app.config['LANGUAGES']:
        return lang

    # Checking if lang is specified in usr configuration (2nd priority)
    user = getattr(g, 'user')
    if user is not None:
        lang = user.get('locale')
        if lang is not None and lang in app.config['LANGUAGES']:
            return lang

    # Checking if lang is specified in header (3rd priority)
    lang = request.args.get('locale')
    if lang is not None and lang in app.config['LANGUAGES']:
        return lang

    # Returning the default lang
    lang = app.config['BABEL_DEFAULT_LOCALE']
    return lang


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """ Gets the users detail """
    user_id = None
    try:
        user_id = int(request.args.get('login_as'))
    except Exception:
        pass
    if user_id is not None:
        if user_id in users:
            return users.get(user_id)
    return None


@app.before_request
def before_request():
    """
    Runs before every other function
    Retrieves the detail of the user
    and assigns it to g
    """
    user = get_user()
    user = setattr(g, 'user', user)


@app.route('/', strict_slashes=False)
def render_index_html():
    """ Renders the 6-index.html """
    user = getattr(g, 'user')
    if user is None:
        logged_in_status = gettext("not_logged_in")
    else:
        logged_in_status = _('logged_in_as', username=user.get('name'))
    return render_template('6-index.html',
                           logged_in_status=logged_in_status,
                           user=user)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
