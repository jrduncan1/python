from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    return redirect('/')

# Make sure this is at the bottom of your server.py file
if __name__=="__main__":
    app.run(debug=True)