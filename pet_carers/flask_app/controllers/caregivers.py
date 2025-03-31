from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.caregiver import Caregiver
from flask_app.models.pet import Pet

@app.route("/")
def index():
    carers = Caregiver.show_all()
    return render_template("index.html", carers = carers)

@app.route("/carer/<int:carer_id>")
def carer(carer_id):
    data = {
        "id": carer_id
    }
    carer = Caregiver.carer_pets(data)
    return render_template("carer.html", carer = carer)

@app.route("/about/<int:carer_id>")
def about(carer_id):
    data = {
        "id": carer_id
    }
    carer = Caregiver.carer_pets(data)
    return render_template("about.html", carer = carer)


@app.route("/create/carer", methods = ["POST"])
def create():
    Caregiver.create_carer(request.form)
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_giver(id):
    print(id)
    data = {
        "id": id
    }
    Caregiver.delete_carer(data)
    return redirect("/")