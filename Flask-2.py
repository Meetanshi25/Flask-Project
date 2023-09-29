# about static and template folder

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/harry")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def about():
    name = "Meetanshiii"
    return render_template('about.html',name2 = name)


app.run(debug=True)