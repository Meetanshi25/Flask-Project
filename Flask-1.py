from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/harry")
def hello_harry():
    return "<p>Hello, harry!</p>"

app.run()