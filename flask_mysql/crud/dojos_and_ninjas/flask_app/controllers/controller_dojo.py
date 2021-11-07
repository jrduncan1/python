from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models import model_dojo

# shows page with all dojos in the database and a form to create a new dojo
# DISPLAY route
@app.route('/')
def index():
    retrieve_dojos = model_dojo.Dojo.all_dojos()
    return render_template("dojos.html", retrieve_dojos=retrieve_dojos)

# processes the new dojo and adds it to db
# ACTION route
@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    model_dojo.Dojo.create(request.form)
    return redirect('/')

# shows page with one dojo's info
# DISPLAY route
@app.route('/dojos/<int:id>')
def show_dojo(id):
    context = {
        'dojos': model_dojo.Dojo.show_ninjas({'id' : id})
    }
    return render_template("dojo_info.html", **context)
