from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/inputs", methods=['GET', 'POST'])
def inputs():
    if request.method == 'POST':
        studentrollno = request.form['studentrollno']
        mailch = request.form['mailch']

        from searchdata import inputnmail
        if mailch == "":
            inputnmail(studentrollno, "n")
        else:
            inputnmail(studentrollno, mailch)

    return render_template("input.html")


@app.route("/results")
def resultroll():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(host="https://attendance-report-and-analytic.herokuapp.com/", debug=True)
