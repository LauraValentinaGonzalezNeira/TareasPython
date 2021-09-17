from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/1")
def primera():
    return render_template("primera.html")

@app.route("/2")
def segunda():
    return render_template("segunda.html")

@app.route("/3")
def tercera():
    return render_template("tercera.html")

if __name__ == '__main--':
    app.run(
        host = '0.0.0.0',
        port = random.random.randint(2000,9000)
    )