from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>\
        <p>EEEE</p>"

@app.route("/name")
@make_bold
def greet():
    return f"Hello!"

if __name__ == "__main__":
    app.run(debug=True)
