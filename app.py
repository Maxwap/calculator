from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Calculator API!"

@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify(result=add(a, b))
    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route('/subtract', methods=['GET'])
def subtract_numbers():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify(result=subtract(a, b))
    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route('/multiply', methods=['GET'])
def multiply_numbers():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify(result=multiply(a, b))
    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route('/divide', methods=['GET'])
def divide_numbers():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        return jsonify(result=divide(a, b))
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
