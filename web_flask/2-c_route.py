#!/usr/bin/python3
"""
    Web Flask Module - Script start a flask app
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome():
    """
        prints the home page
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        prints the hbnb page
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
        Using Variables for routing
    """
    return "C {:s}".format(text).replace('_', ' ')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
