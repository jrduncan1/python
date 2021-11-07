from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_dojo, model_ninja

# form page that allows client to create new Ninja
# DISPLAY route
@app.route('/ninja/new')
def new_ninja():
    context = {
        'all_dojos': model_dojo.Dojo.all_dojos()
    }
    return render_template("ninja_new.html", **context)


# processes the new ninja and adds it to the db
@app.route('/ninja/create', methods=["POST"])
def create_ninja():
    dojo_id = request.form['dojo_id']
    model_ninja.Ninja.create(request.form)
    return redirect(f'/dojos/{dojo_id}')

