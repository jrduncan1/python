from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_user, model_recipe
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

## Display route______________________________________________________
# Login/registration page--if user is logged in(and didn't log out), directs them straight to the dashboard
@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('index.html')

## Action route_______________________________________________________
# Processes the registration of a new user
@app.route('/register', methods = ["POST"])
def register():
    if not model_user.User.registration_validate(request.form):
        return redirect('/')
    
    hash_slinging_slasher = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hash_slinging_slasher
    }
    user_id = model_user.User.create_user(data)
    session['uuid'] = user_id

    return redirect('/dashboard')

# Logs user out
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# Logs user in
@app.route('/login', methods = ["POST"])
def login():
    if not model_user.User.login_validate(request.form):
        return redirect('/')

    user = model_user.User.retrieve_user_with_email({'email': request.form['email']})

    session['uuid'] = user.id

    return redirect('/dashboard')