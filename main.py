from os import path

from flask import Flask, render_template, request
from flask_cors import CORS

from waitress import serve

BASE_DIR = path.dirname(__file__)

app = Flask(
    __name__,
    template_folder="dist",
    static_folder="dist/static",
)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000)
    serve(app, host='0.0.0.0', port=5000)