from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Environment variable for the real backend base URL
REAL_BACKEND = os.environ.get("REAL_BACKEND", "http://localhost:5000")

# Route: Home
@app.route("/", methods=["GET"])
def home():
    return {"message": "Proxy is working!"}, 200

# Route: Forward GET /unpicked-orders
@app.route("/unpicked-orders", methods=["GET"])
def unpicked_orders():
    try:
        res = requests.get(f"{REAL_BACKEND}/unpicked-orders")
        return jsonify(res.json()), res.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Forward PUT /update-order-status/<order_id>
@app.route("/update-order-status/<order_id>", methods=["PUT"])
def update_order_status(order_id):
    try:
        data = request.get_json()
        res = requests.put(f"{REAL_BACKEND}/update-order-status/{order_id}", json=data)
        return jsonify(res.json()), res.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Forward GET /picked-orders-history/<user_id>
@app.route("/picked-orders-history/<user_id>", methods=["GET"])
def picked_history(user_id):
    try:
        res = requests.get(f"{REAL_BACKEND}/picked-orders-history/{user_id}")
        return jsonify(res.json()), res.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Forward POST /add-product
@app.route("/add-product", methods=["POST"])
def add_product():
    try:
        data = request.get_json()
        res = requests.post(f"{REAL_BACKEND}/add-product", json=data)
        return jsonify(res.json()), res.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Forward GET /seller-products/<user_id>
@app.route("/seller-products/<user_id>", methods=["GET"])
def seller_products(user_id):
    try:
        res = requests.get(f"{REAL_BACKEND}/seller-products/{user_id}")
        return jsonify(res.json()), res.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
