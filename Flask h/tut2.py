# # in flask static is public and tampletes are by default private
# from flask import Flask, render_template

# app = Flask(__name__)


# @app.route("/")
# def hello():
#     return render_template('index.html')


# @app.route("/about")
# def vedant():
#     name = "vedant"
#     return render_template('about.html', name2=name)


# @app.route("/bootstrap")
# def bootstrap():
#     return render_template('bootstrap.html')


# # debug=True is for detect change and reload the website
# app.run(debug=True)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def run_script():
    file = open(r'E:\Flask h\game.py', 'r').read()
    return exec(file)


if __name__ == "__main__":
    app.run(debug=True)
