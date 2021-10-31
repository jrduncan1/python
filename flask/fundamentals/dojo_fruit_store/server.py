from flask import Flask, render_template, request, redirect, session
from datetime import datetime
app = Flask(__name__)

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    session['raspberry_count'] = request.form['raspberry']
    session['strawberry_count'] = request.form['strawberry']
    session['apple_count'] = request.form['apple']
    session['blackberry_count'] = request.form['blackberry']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    session['count'] = int(['strawberry_count'])+int(['raspberry_count'])+int(['apple_count'])+int(['blackberry_count'])
    session['date'] = datetime.now()
    print("Charging", session['first_name'], session['last_name'], "for", session['count'], "fruits on", session['date'], ".")
    return render_template("checkout.html")

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    