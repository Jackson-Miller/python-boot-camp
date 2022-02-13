from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>" \
           "<p>This is a paragraph.</p>" \
           "<img src='https://media.giphy.com/media/cJfY82h8ijUFQEmDKa/giphy.gif'>"


@app.route("/admin")
@make_bold
@make_underlined
@make_emphasis
def admin_login():
    return "Login below!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<h1>Hello {name.title()}, you are {number}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
