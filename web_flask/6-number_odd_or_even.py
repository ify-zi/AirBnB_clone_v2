#!/usr/bin/python3
"""
    Web Flask Module - Script start a flask app
"""

from flask import Flask, render_template


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


@app.route('/number/<int:n>')
def number_func(n):
    """check for number and return page"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def temp(n):
    """
        function renders html tags if number is true
    """
    val = {'n': n}
    return render_template('5-number.html', **val)


@app.route('/number_odd_or_even/<int:n>')
def modu(n):
    """
        function renders if a value is odd or even
    """
    val = {'n': n}
    return render_template('6-number_odd_or_even.html', **val)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
