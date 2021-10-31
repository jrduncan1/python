from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'dolphins'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect("/show")

@app.route("/show")
def show_user():
    print("Sowing the User Info from the Form")
    return render_template("show.html", name_on_template=session['username'], email_on_template=['useremail'])

# Make sure this is at the bottom of your server.py file
if __name__=="__main__":
    app.run(debug=True)