from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.recipe_model import Recipe
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt
from flask import flash
bcrypt = Bcrypt(app)

#-------------Render - Create a Recipe-------------

@app.route('/recipe/new')
def new_recipe():
    return render_template("recipe_new.html")

#---------------Create a Recipe-------------------

@app.route('/create/recipe', methods = ["POST"])
def create_recipe():
    print(request.form)
    if not Recipe.validate(request.form):
        return redirect('/recipe/new')
    recipe_data = {
        **request.form,
        'user_id' : session['user_id']
    }
    Recipe.create(recipe_data)
    return redirect('/dashboard')

#---------------Render - Display One Recipe-----------------

@app.route('/recipes/<int:id>')
def show_one_recipe(id):
    this_recipe = Recipe.get_by_id({'id': id})
    data = {
        'id' : session['user_id']
    }
    logged_user = User.get_one(data)
    return render_template("recipe_show.html", this_recipe = this_recipe, logged_user=logged_user)

#---------------Render - Update/Edit Recipe-------------

@app.route('/recipes/<int:id>/edit')
def edit_recipe(id):
    this_recipe = Recipe.get_by_id({'id':id})
    return render_template("recipe_edit.html", this_recipe = this_recipe)

#-------------Update/Edit a Recipe-----------------

@app.route('/recipe/<int:id>/update', methods = ['post'])
def update_recipe(id):
    if not Recipe.validate(request.form):
        return redirect(f"/recipes/{id}/edit")
    update_data = {
        **request.form,
        'id': id
    }
    Recipe.update(update_data)
    return redirect('/dashboard')

#----------------Delete Recipe-----------------

@app.route('/recipes/<int:id>/delete')
def delete(id):
    Recipe.delete({'id':id})
    return redirect('/dashboard')