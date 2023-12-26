#!/usr/bin/python3

"""starts a Flask web application"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays hello hbnb"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    """Displays c is followed by the value of the text"""
    formatted_text = escape(text).replace("_", " ")
    return f"C {formatted_text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is(text="is cool"):
    """Displays Python is followed by the value of the text"""
    formatted_text = escape(text).replace("_", " ")
    return f"Python {formatted_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """Displays 'n is a number' only if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Displays an HTML page only if n is an integer.

    Args:
        n (int): number to be displayed
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Displays an HTML page only if n is an integer.

    Args:
        n (int): number to be displayed
    """
    if n % 2 != 0:
        return render_template("6-number_odd_or_even.html", n=n, result="odd")
    else:
        return render_template("6-number_odd_or_even.html", n=n, result="even")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
