from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_user, model_recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

## Display route______________________________________________________
@app.route('/new')
def create():
    return render_template("new_recipe.html")

@app.route('/dashboard')
def dashboard():
    if 'uuid' in session:
        all_recipes = model_recipe.Recipe.retrieve_all_recipes(request.form)
        user = model_user.User.retrieve_user_with_id({'id': session['uuid']})
        return render_template('dashboard.html', all_recipes = all_recipes, user=user)
    return redirect('/')

@app.route('/show_recipe/<int:id>')
def show_recipe(id):
    recipe = model_recipe.Recipe.retrieve_one_recipe({'id': id})
    return render_template('show_recipe.html', recipe = recipe)



## Action route_______________________________________________________
@app.route('/process_recipe', methods=["POST"])
def process():
    if not model_recipe.Recipe.recipe_validate(request.form):
        return redirect('/new')
    else:
        data = {
        **request.form,
        "user_id": session["uuid"]
        }
        model_recipe.Recipe.create_recipe(data)
        return redirect('/dashboard')