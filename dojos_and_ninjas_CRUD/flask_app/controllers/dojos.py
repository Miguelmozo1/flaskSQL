from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos)

@app.route('/new/dojo', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def display_dojo(id):
    data = {
        "id": id
    }
    session["id"] = id
    print(session["id"])
    return render_template("dojo.html", dojo = Dojo.display_one_ninjas(data), ninja = Ninja)