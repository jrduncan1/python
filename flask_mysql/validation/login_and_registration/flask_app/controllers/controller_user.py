from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_user
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

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

    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html', user = model_user.User.retrieve_with_id({'id': session['uuid']}))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/login', methods = ["POST"])
def login():
    if not model_user.User.login_validate(request.form):
        return redirect('/')

    user = model_user.User.retrieve_with_email({'email': request.form['email']})

    session['uuid'] = user.id

    return redirect('/success')
