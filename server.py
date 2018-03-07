from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/ninja")
def ninjas():
    return render_template("ninjas.html")
@app.route("/ninja/<color>")
def ninja(color):
    if color == "blue":
        return render_template("ninja.html", ninja="leonardo.jpg")
    elif color == "orange":
        return render_template("ninja.html", ninja="michelangelo.jpg")
    elif color == "red":
        return render_template("ninja.html", ninja="raphael.jpg")
    elif color == "purple":
        return render_template("ninja.html", ninja="donatello.jpg")
    else:
        return render_template("ninja.html", ninja="notapril.jpg")
app.run(debug=True)