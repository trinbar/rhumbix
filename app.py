import flask
from flask import Flask, request, json, jsonify, make_response, render_template
import requests  # for calling 3rd party API


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/gif', methods=['GET'])
def get_gifs():
    """Renders gif"""

    keyword = request.form["keyword"]

    res = requests.get('http://api.giphy.com/v1/gifs/search?q='+ keyword + '&api_key=DLCVuTK6KZExOS7JoMq82bi5MaI6EbWO&limit=1')
    data = res.json()
    gif= data["images"]["downsized_large"]["url"]

    return render_template("gif.html", gif=gif)


if __name__ == "__main__":
    app.run(debug=True)