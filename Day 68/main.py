from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'JVhxI_CTHtKIDQiaa5Qgfg2oMV6CKZqW2FSkRTxeXFY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

ph = PasswordHasher()
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.context_processor
def inject_user():
    return dict(logged_in=current_user.is_authenticated)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if the user already exist
        user = User.query.filter_by(email=request.form.get("email")).first()

        if user is not None:
            flash("An account already exist for this email address.")
        else:
            new_user = User(
                email=request.form.get("email"),
                password=ph.hash(request.form.get("password")),
                name=request.form.get("name")
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return render_template("secrets.html", user)

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")

        user = User.query.filter_by(email=email).first()

        if user is None:
            flash("Invalid username or password.")
        else:
            try:
                pw_verifier = ph.verify(user.password, request.form.get("password"))
            except VerifyMismatchError:
                pw_verifier = False

            if pw_verifier:
                login_user(user)
                return render_template("secrets.html", name=user.name)
            else:
                flash("Invalid username or password.")

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory='static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
