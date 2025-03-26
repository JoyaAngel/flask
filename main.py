from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Yop" : "123456", "Yopi": "78945612", "Lana del rey": "125485489"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
