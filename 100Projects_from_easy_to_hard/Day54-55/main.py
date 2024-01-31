from flask import Flask
import random

n = random.randint(0,9)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>\
        <img src='https://media1.giphy.com/media/LfbDxyQIWtzLTtMnc0/200w.gif?cid=82a1493bzii7ihsp35f0cv0cwvpnr4hdvl3f1hc5le2gh4rf&ep=v1_gifs_related&rid=200w.gif&ct=g'>"

@app.route("/<int:num>")
def number(num):
    if num<n: return f"<h1>{num} is too low, try again</h1>\
        <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif num>n: return f"<h1>{num} is too high, try again</h1>\
        <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif num == n : return f"<h1>{num} is correct</h1>\
        <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug = True)