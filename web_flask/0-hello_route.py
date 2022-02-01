#!/usr/bin/python3

""" this applications has one route
    it listens on 0.0.0.0:500
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    # Display Hello HBNB
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
