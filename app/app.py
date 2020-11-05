from flask import Flask

app = Flask(__name__)

if __name__=="_main_":
    app.run()

@app.route("/")
def hello():
    return "Hello World"