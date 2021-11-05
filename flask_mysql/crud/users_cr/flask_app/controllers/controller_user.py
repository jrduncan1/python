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

# form page that allows you to create new user
# DISPLAY route
@app.route('/users/new')
def new_user():
    return render_template('users_new.html')

# processes the new user and adds it to db
# ACTION route
@app.route('/users/create', methods=['POST'])
def create_user():
    id = model_user.User.create(request.form)
    return redirect('/')


