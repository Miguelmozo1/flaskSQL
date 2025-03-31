from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.pet import Pet
from flask_app.controllers import caregivers


@app.route("/create/pet", methods = ["POST"])
def create_pet():
    Pet.create_pet(request.form)
    return redirect(f"/carer/{request.form["caregiver_id"]}")