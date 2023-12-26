#!/usr/bin/python3

"""starts a Flask web application"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_hello_hbnb():
    """Displays hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """Displays hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c_is(text):
    """Displays c is followed by the value of the text"""
    formatted_text = escape(text).replace("_", " ")
    return f"C {formatted_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
