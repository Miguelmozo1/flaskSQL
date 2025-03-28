from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models.user import User

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register', methods=['POST'])
def create_user():
    if not User.validate_register(request.form):
        return redirect('/')
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.register(data)
    session["user_id"] = id
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    if "user_id" not in session:
        return redirect('/logout')
    data = {
        "id": session['user_id']
    }
    return render_template("welcome.html", user = User.get_by_id(data))

@app.route('/login', methods = ['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user:
        flash("Invalid email", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/welcome')




@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
