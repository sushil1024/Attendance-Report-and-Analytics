from flask import Flask, render_template, request, redirect

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
        email = request.form['email']

        from searchdata import inputroll
        inputroll(studentrollno)

    return render_template("input.html")


if __name__ == "__main__":
    app.run(debug=True)
