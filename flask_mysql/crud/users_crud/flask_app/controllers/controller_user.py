from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import model_user

# shows page with all users in the database
# DISPLAY route
@app.route('/')
@app.route('/users')
def all_users():
    retrieve_users = model_user.User.get_all()
    return render_template("users_all.html", retrieve_users=retrieve_users)

# page with form that allows you to create new user
# DISPLAY route
@app.route('/users/new')
def new_user():
    return render_template('users_new.html')

# processes the new user and adds it to db
# ACTION route
@app.route('/users/create', methods=['POST'])
def create_user():
    id = model_user.User.create(request.form)
    return redirect(f'/users/{id}')

# shows page with one user's info
# DISPLAY route
@app.route('/users/<int:id>')
def show_one(id):
    context = {
        'users': model_user.User.get_one({'id': id})
    }
    return render_template("users_one.html", **context)

# shows page where user can update user info
# DISPLAY route
@app.route('/users/<int:id>/edit')
def edit_user(id):
    context = {
    'users': model_user.User.get_one({'id': id})
    }
    return render_template('users_edit.html', **context)

# processes updating of user info
# ACTION route
@app.route('/users/<int:id>/update', methods=['POST'])
def update_user(id):
    data = {
        **request.form,
        'id': id
    }
    model_user.User.update_one(data)
    return redirect(f'/users/{id}')

# deletes a user
# ACTION route
@app.route('/users/<int:id>/delete')
def delete_user(id):
    model_user.User.delete_one({'id': id})
    return redirect('/')
