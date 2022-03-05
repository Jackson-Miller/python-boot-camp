import os
import secrets
from dotenv import load_dotenv
from forms import EditRating, AddMovie
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import requests

load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_bytes(32)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-10-movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


def search_movies(movie_name):
    uri = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=en-US&query={movie_name}"
    response = requests.get(uri)
    return response.json()


def get_movie(movie_id):
    uri = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
    response = requests.get(uri)
    return response.json()


@app.route("/")
def home():
    movie_list = Movie.query.all()
    for i in range(len(movie_list)):
        movie_list[i].ranking = len(movie_list) - i
    db.session.commit()
    return render_template("index.html", movies=movie_list)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovie()
    if request.method == "POST":
        if form.validate_on_submit():
            results = search_movies(form.title.data)
            return render_template("select.html", movies=results["results"])
    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditRating()
    if request.method == "POST":
        movie_id = request.args.get("id")
        movie_to_update = Movie.query.get(movie_id)
        if form.validate_on_submit():
            movie_to_update.rating = float(form.rating.data)
            movie_to_update.review = form.review.data
            db.session.commit()
            return redirect(url_for('home'))

    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/search")
def search():
    movie_id = request.args.get('id')
    movie_details = get_movie(movie_id)
    new_movie = Movie(
        id=movie_id,
        title=movie_details["original_title"],
        year=movie_details["release_date"].split("-")[0],
        description=movie_details["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500/{movie_details['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=movie_id))


if __name__ == '__main__':
    app.run()
