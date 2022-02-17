import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    blog_data = requests.get("https://api.npoint.io/0bc6d10890d465b9b158")
    all_post = blog_data.json()
    return render_template("index.html", posts=all_post)


@app.route('/post/<post_id>')
def display_post(post_id):
    blog_data = requests.get("https://api.npoint.io/0bc6d10890d465b9b158")
    post = blog_data.json()[int(post_id) - 1]
    return render_template("post.html", post=post)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
