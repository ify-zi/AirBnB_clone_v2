#!/usr/bin/python3
"""
    Web Flask Module - Script start a flask app
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome():
    """
        prints the home page
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
