#!/usr/bin/python3
"""
    Web Flask Module - Script start a flask app
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)
""" Instantiation of the code """
app.url_map.strict_slashes = False


@app.route('/')
def welcome():
    """
        prints the home page
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """
        prints the hbnb page
    """
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """
        Using Variables for routing
    """
    return "C {:s}".format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python', defaults={"text": "is cool"})
def python_func(text):
    """
        printing varaible swith conditions
    """
    return "Python {:s}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
