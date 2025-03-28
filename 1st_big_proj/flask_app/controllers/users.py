from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.magazine import Magazine
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')
    
    data = {"email": request.form['email']}
    user_in_db = User.get_one_by_email(data)
    if user_in_db:
        flash("Email already exists!")
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "first_name": request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email'],
        "password" : pw_hash,
    }

    user_id = User.save(data)
    session['user_id'] = user_id
    return redirect("/dashboard")

@app.route('/login',methods=['POST'])
def login():
    data = {"email": request.form['email']}
    user_in_db = User.get_one_by_email(data)
    if not user_in_db:
        flash("Invalid Email", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password,request.form['password']):
        flash("Invalid Password", "login")
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please Log In!')
        return redirect('/')
    data = {
        "id": session["user_id"]
    }
    magazines = Magazine.get_all_w_creator()
    return render_template('dashboard.html',magazines=magazines, user = User.get_by_id(data))


@app.route('/user/<int:id>/edit')
def edit_page(id):
    if 'user_id' not in session:
        flash('Please Log In!')
        return redirect('/')
    data = {
        "id":id
    }
    
    user = User.get_by_id(data)
    magazines = Magazine.get_all_w_creator()
    return render_template('update_user.html', user=user, magazines = magazines )

@app.route('/user/<int:id>/edit',methods=['POST'])
def edit_user(id):
    if 'user_id' not in session:
        flash('Please Log In!')
        return redirect('/')
    data = {
        "id":id,
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email']
    }
    User.update(data)
    return redirect('/dashboard')



