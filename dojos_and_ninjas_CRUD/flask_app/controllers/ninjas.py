from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import dojo, ninja
from flask_app.models.ninja import Ninja

@app.route('/new/ninja')
def ninjas():
    return render_template("ninja.html", dojos = dojo.Dojo.get_all())

@app.route("/delete/<ninja_id>")
def delete(ninja_id):
    data = {
        "id": ninja_id
    }
    ninja.Ninja.delete(data)
    return redirect(request.referrer)

@app.route("/ninja/update/<int:ninja_id>")
def ninja_update(ninja_id):
    data = {
        "id": ninja_id
    }
    ninja = Ninja.get_ninja_by_id(data)
    return render_template("edit_ninja.html", ninja = ninja )

@app.route("/update/ninja/<int:id>", methods = ["POST"])
def update_ninja(id):
    data = {
        "id": id,
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"]
    }
    Ninja.update_ninja(data)
    return redirect(f"/dojo/{session["id"]}")

@app.route('/create/ninja', methods = ['POST'])
def create():
    ninja.Ninja.save(request.form)
    return redirect("/")