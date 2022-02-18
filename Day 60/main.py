from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        return render_template("login.html", username=request.form['username'], password=request.form['password'])


if __name__ == "__main__":
    app.run()
