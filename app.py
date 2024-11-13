import urllib.request
from flask import Flask

app = Flask(__name__)


def is_it_raining_in_seattle():
    with urllib.request.urlopen('https://depts.washington.edu/ledlab/teaching/is-it-raining-in-seattle/') as response:
        is_it_raining_in_seattle = response.read().decode()

    return is_it_raining_in_seattle == "true"


@app.route("/")
def index():
    if is_it_raining_in_seattle():
        return "<h1>Yes</h1>"
    else:
        return "<h1>No</h1>"


if __name__ == "__main__":
    app.run(debug=True)
