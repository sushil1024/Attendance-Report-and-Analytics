
def deleteres():
    with open("templates/result.html", "w") as f:
        f.write("<h1>No inputs yet!</h1>")
        f.write('<a href="/inputs">Go back</a>')
