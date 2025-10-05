from flask import Flask, request, jsonify
from uuid import uuid4

def validate_product_data(data):
    """Validate product data and return errors if any"""
    errors = []
    
    # Check required fields
    if 'name' not in data or not data['name'] or data['name'].strip() == '':
        errors.append("Product name is required and cannot be empty")
    elif len(data['name']) > 100:
        errors.append("Product name must be 100 characters or less")
    
    if 'price' not in data:
        errors.append("Price is required")
    elif not isinstance(data['price'], (int, float)):
        errors.append("Price must be a number")
    elif data['price'] <= 0:
        errors.append("Price must be greater than 0")
    
    if 'stock' not in data:
        errors.append("Stock is required")
    elif not isinstance(data['stock'], int):
        errors.append("Stock must be an integer")
    elif data['stock'] < 0:
        errors.append("Stock must be non-negative")
    
    # Check optional fields
    if 'description' in data and data['description'] and len(data['description']) > 500:
        errors.append("Description must be 500 characters or less")
    
    if 'category' in data and data['category'] and len(data['category']) > 50:
        errors.append("Category must be 50 characters or less")
    
    return errors
app = Flask(__name__)
# Hashmap storage
products = {}

@app.route('/', methods=['GET'])
def root():
        return jsonify({
        "message": "Product API is running",
        "version": "1.0.0",
        "endpoints": {
            "GET /products": "Retrieve all products",
            "GET /products/<id>": "Retrieve a specific product",
            "POST /products": "Create a new product"
        }
    }), 200

@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(list(products.values())), 200

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400
    
    errors = validate_product_data(data)
    if errors:
        return jsonify({"errors": errors}), 422
    
# Create product
    product_id = str(uuid4())
    product = {
        "id": product_id,
        "name": data['name'].strip(),
        "description": data.get('description'),
        "price": round(float(data['price']), 2),
        "stock": int(data['stock']),
        "category": data.get('category')
    }
    products[product_id] = product
    return jsonify(product), 201

@app.route("/products/<product_id>", methods=["GET"])
def get_product(product_id):
    if product_id not in products:
        return jsonify({
            "error": f"Product with id '{product_id}' not found"
        }), 404
    return jsonify(products[product_id]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)