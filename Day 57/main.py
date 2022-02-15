import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    blog_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_post = blog_data.json()
    return render_template("index.html", posts=all_post)


@app.route('/post/<post_id>')
def display_post(post_id):
    blog_data = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    post = blog_data.json()[int(post_id) - 1]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run()
