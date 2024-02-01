from flask_app import app
from flask_app.models.user import User
from flask import render_template, redirect, request

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/roster")
def show_all():
    return render_template("roster.html", users = User.show_all())




@app.route("/reg", methods=["POST"])
def create_user():
    User.create_user(request.form)
    return redirect("/roster")