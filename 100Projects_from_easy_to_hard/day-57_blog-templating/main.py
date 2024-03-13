from flask import Flask, render_template
import requests
from post import Post
app = Flask(__name__)

@app.route('/')
def home():
    x = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    return render_template("index.html", data = x)

@app.route("/post/<id>")
def post(id):
    x = Post(id)
    y = x.get()
    print(y)
    return render_template("post.html", x = y)
if __name__ == "__main__":
    app.run(debug=True)
