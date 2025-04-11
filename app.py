from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample data for demonstration
sample_deals = [
    {"id": 1, "store": "Kroger", "item": "Apples", "price": 1.99, "unit": "lb"},
    {"id": 2, "store": "Walmart", "item": "Bananas", "price": 0.49, "unit": "lb"},
    {"id": 3, "store": "Target", "item": "Milk", "price": 2.99, "unit": "gallon"}
]

@app.route('/')
def home():
    return jsonify({"status": "ok", "message": "Grocery Deal Finder API is running"})

@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    # Simple filtering based on query
    results = [deal for deal in sample_deals if query.lower() in deal['item'].lower()]
    return jsonify({
        "results": results,
        "count": len(results),
        "query": query
    })

@app.route('/api/stores', methods=['GET'])
def stores():
    # Return unique stores
    unique_stores = list(set(deal['store'] for deal in sample_deals))
    return jsonify({
        "stores": unique_stores
    })

@app.route('/api/upload', methods=['POST'])
def upload():
    # Simulate file upload processing
    return jsonify({
        "success": True,
        "message": "File uploaded successfully"
    })

@app.route('/api/compare', methods=['POST'])
def compare():
    # Simulate comparison
    data = request.json
    items = data.get('items', [])
    return jsonify({
        "results": [
            {
                "item": item,
                "bestDeal": {
                    "store": "Kroger",
                    "price": 1.99
                },
                "alternatives": [
                    {"store": "Walmart", "price": 2.49},
                    {"store": "Target", "price": 2.99}
                ]
            } for item in items
        ]
    })

# This is important for Vercel
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
  
