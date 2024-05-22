# in flask static is public and tampletes are by default private

import egg_catcher.py  # **
from distutils.log import debug
from unicodedata import name
from flask import Flask, render_template

app = Flask(__name__)


# @app.route("/")
# def func(egg_catcher):
#     return egg_catcher.py


# @app.route("/")
# def hello_world():
#     return render_template('index.html')


@app.route("/")
def vedant():
    name = "vedant"
    # egg_catcher.py
    egg_catcher.create_eggs()  # **
    return render_template(name2=name)


# debug=True is for detect change and reload the website
app.run(debug=True)
