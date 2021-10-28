from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say(name):
    return "Hi, " + name

@app.route('/<text>/<int:num>')
def mult(text, num):
    return f"{text * num}"

if __name__ == "__main__":
    app.run(debug = True)