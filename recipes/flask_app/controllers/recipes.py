from flask import request, render_template, redirect, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/welcome')
def recipes_home():
    if "user_id" not in session:
        flash("You must be logged in to access the homepage")
        return redirect('/')
    user = User.get_by_id(session['user_id'])
    recipes = Recipe.get_all()
    return render_template("welcome.html", user = user, recipes = recipes)

@app.route('/recipes/<recipe_id>')
def recipe_details(recipe_id):
    recipe = Recipe.recipe_by_id(recipe_id)
    return render_template("single_recipe.html", recipe = recipe)

@app.route('/recipes/new')
def create_page():
    data = {
        'id': session['user_id']
    }
    return render_template('create_recipe.html', user = User.get_by_id(data))

@app.route('/recipes/edit/<recipe_id>')
def edit_page(recipe_id):
    recipe = Recipe.recipe_by_id(recipe_id)
    return render_template("edit_recipe.html", recipe = recipe)

@app.route('/recipes/delete/<recipe_id>')
def delete_recipe(recipe_id):
    print('hello', recipe_id)
    return redirect('/welcome')

@app.route('/recipes/create', methods=["POST"])
def create_recipe():
    print(request.form)
    Recipe.create_recipe(request.form)
    return redirect('/welcome')

app.route('/recipes/update')
def update_recipe():
    return redirect('/welcome')