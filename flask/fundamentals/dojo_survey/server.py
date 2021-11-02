from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "dolphin"

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/process', methods=["POST"])
def process_form():
    session['full_name'] = request.form['full_name']
    session['dojo_location'] = request.form['dojo_location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')

# Make sure this is at the bottom of your server.py file
if __name__=="__main__":
    app.run(debug=True)