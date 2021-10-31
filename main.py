from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route("/inputs", methods=['GET', 'POST'])
def input():
    return render_template("input.html")


if __name__ == "__main__":
    app.run(debug=True)
