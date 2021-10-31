from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "dolphin"

@app.route('/')
def init():
    if 'count' in session:
        session['count'] = session['count'] + 1
    else:
        session['count'] = 0
    return render_template("index.html")

@app.route('/destroy_session')
def reset():
    session.pop('count')
    return redirect('/')

@app.route('/plus2')
def plus():
    session['count'] = session['count'] + 1
    return redirect('/')

# Make sure this is at the bottom of your server.py file
if __name__=="__main__":
    app.run(debug=True)