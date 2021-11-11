from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_user, model_recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

## Display route______________________________________________________
# Directs user to page where they can create recipe
@app.route('/new')
def create():
    return render_template("new_recipe.html")

# Takes logged-in users to dashboard where they can view recipes and edit/delete their own. If user is not logged in and in session, redirects to login/reg page
@app.route('/dashboard')
def dashboard():
    if 'uuid' in session:
        all_recipes = model_recipe.Recipe.retrieve_all_recipes(request.form)
        user = model_user.User.retrieve_user_with_id({'id': session['uuid']})
        return render_template('dashboard.html', all_recipes = all_recipes, user=user)
    return redirect('/')

# Shows info for selected recipe
@app.route('/show_recipe/<int:id>')
def show_recipe(id):
    recipe = model_recipe.Recipe.retrieve_one_recipe({'id': id})
    return render_template('show_recipe.html', recipe = recipe)

# Directs logged in users who created the recipe in question, to a page that allows them to edit and update their recipe info.
@app.route('/edit_recipe/<int:id>')
def edit_recipe(id):
    if 'uuid' in session:
        data = {'id': id}
        recipe = model_recipe.Recipe.retrieve_one_recipe(data)
        session['recipe_id'] = id
        return render_template('edit_recipe.html', recipe = recipe)
    return redirect('/')



## Action route_______________________________________________________
# Processes creation of new recipe
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

# Processes updating of new recipe
@app.route('/update_recipe/<int:id>', methods=["POST"])
def update(id):
    recipe_id = session['recipe_id']
    if not model_recipe.Recipe.recipe_validate(request.form):
        return redirect(f'/edit_recipe/{recipe_id}')
    data = {
        **request.form,
        'id': id
    }
    model_recipe.Recipe.edit_recipe(data)
    return redirect('/dashboard')

# Processes deleting of recipe
@app.route('/delete_recipe/<int:id>')
def delete_recipe(id):
    model_recipe.Recipe.delete_recipe({'id': id})
    return redirect('/dashboard')
