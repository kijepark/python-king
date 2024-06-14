from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/text", methods=["GET"])
def text():
    return "Hello, World!"


@app.route("/json", methods=["GET"])
def json():
    return jsonify({"message": "Hello, World!"})


if __name__ == "__main__":
    app.run()
