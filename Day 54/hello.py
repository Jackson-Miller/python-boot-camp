from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/admin")
def admin_login():
    return "<p>Login below!</p>"


if __name__ == "__main__":
    app.run()
