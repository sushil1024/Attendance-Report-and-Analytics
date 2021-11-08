from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route("/")
def home():
    if os.path.exists("templates/result.html"):
        os.remove("templates/result.html")
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@app.route("/inputs", methods=['GET', 'POST'])
def inputs():
    if request.method == 'POST':
        studentrollno = request.form['studentrollno']
        mailch = request.form['mailch']

        from searchdata import inputnmail
        inputnmail(studentrollno, mailch)

    return render_template("input.html")


@app.route("/results")
def resultstu():
    if os.path.exists("templates/result.html"):
        return render_template("result.html")

    else:
        return "<h1>Details about the candidate will be shown here</h1>"


if __name__ == "__main__":
    app.run(debug=True)
