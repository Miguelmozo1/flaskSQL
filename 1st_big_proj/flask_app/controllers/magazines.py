from flask import Flask, render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.magazine import Magazine
from flask_app.models.user import User


@app.route('/magazine/new')
def magazine_form():
    if 'user_id' not in session:
        flash('Please Log In!')
        return redirect('/')
    data = {
        "id":session['user_id']
    }
    user = User.get_by_id(data)
    return render_template('new_magazine.html', user = user)

@app.route('/magazine', methods=['POST'])
def create_magazine():
    if 'user_id' not in session:
        flash('Please Log In!')
        return redirect('/')
    if not Magazine.validate_magazine(request.form):
        flash("Title must be at least 2 characters or description more than 10 characters!", "magazine")
        return redirect('/magazine/new')
    data = {
        "title":request.form['title'],
        "description":request.form['description'],
        "user_id": session['user_id']
    }
    Magazine.validate_magazine(data)
    Magazine.save(data)
    return redirect('/dashboard')


@app.route('/magazine/<int:id>/delete')
def delete(id):
    if 'user_id' not in session:
        flash('Please Log In!')
        return redirect('/')
    data = {
        "id":id
    }
    Magazine.delete(data)
    return redirect('/dashboard')

@app.route('/magazine/<int:id>')
def show_page(id):
    if 'user_id' not in session:
        flash('Please Log In!')
        return redirect('/')
    data = {
        "id": id
    }
    data_2 = {
        "id":session['user_id']
    }
    user = User.get_by_id(data_2)
    magazine = Magazine.get_one_by_id(data)
    return render_template('magazine.html', magazine = magazine, user = user)