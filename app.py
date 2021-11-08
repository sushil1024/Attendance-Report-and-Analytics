from flask import Flask, render_template, request
import sys

app = Flask(__name__)


@app.route("/")
def home():
    from resetresult import deleteres
    deleteres()
    del sys.modules['resetresult']
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    from resetresult import deleteres
    deleteres()
    del sys.modules['resetresult']
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
def resultroll():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
