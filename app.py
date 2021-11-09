
# Document: Attendance Report and Analytics
# Created on: October 17, 2021, 9:00:00 PM
# Last Updated: November 9, 2021. 8:00:00 AM
# Author: Sushil Waghmare


from flask import Flask, render_template, request

app = Flask(__name__)


# the home page
@app.route("/")
def home():
    return render_template("home.html")


# authentication page
@app.route("/login")
def login():
    return render_template("login.html")


# input page to input roll number of the candidate
@app.route("/inputs", methods=['GET', 'POST'])
def inputs():
    if request.method == 'POST':

        # takes input here in post method
        studentrollno = request.form['studentrollno']
        mailch = request.form['mailch']

        # taken inputs will be passed to another function for further process
        from searchdata import inputnmail
        inputnmail(studentrollno, mailch)

    return render_template("input.html")


if __name__ == "__main__":
    app.run(debug=True)
