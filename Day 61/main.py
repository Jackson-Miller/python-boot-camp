import secrets
from forms import LoginForm
from flask_bootstrap import Bootstrap
from flask import Flask, request, render_template

app = Flask(__name__)
app.secret_key = secrets.token_bytes(32)
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.validate_on_submit():
            if form.email.data == "admin@email.com" and form.password.data == "1234567890":
                return render_template("success.html")
            else:
                return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
