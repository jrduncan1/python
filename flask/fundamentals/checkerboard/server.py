from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def level_1():
    return render_template("index.html", num=8, num2=8)

@app.route('/<int:num>')
def level_2(num):
    return render_template("index.html", num=num, num2=8)

@app.route('/<int:num>/<int:num2>')
def level_3(num,num2):
    return render_template("index.html", num=num, num2=num2)

if __name__=="__main__":
    app.run(debug=True)