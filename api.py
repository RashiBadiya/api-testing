# app_complex.py
# This is a more complex API that simulates a simple CRUD (Create, Read, Update, Delete)
# operation on a collection of "items".

from flask import Flask, jsonify, request, abort

# Create an instance of the Flask class.
app = Flask(__name__)

# This list will act as our in-memory "database".
items = [
    {"id": 1, "name": "Apple", "price": 1.00, "quantity": 50},
    {"id": 2, "name": "Banana", "price": 0.50, "quantity": 120},
    {"id": 3, "name": "Cherry", "price": 2.50, "quantity": 30}
]

# This variable will be used to generate new, unique IDs for new items.
next_id = 4

# --- GET home page ---
# This is a new route that will be displayed when you visit the root URL.
@app.route('/', methods=['GET'])
def home():
    """
    Displays a simple HTML page confirming the API is running.
    """
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>API Status</title>
        <style>
            body { font-family: sans-serif; text-align: center; margin-top: 50px; background-color: #f0f4f8; color: #334e68; }
            h1 { color: #2a6a9b; }
            a { color: #1e70bf; text-decoration: none; font-weight: bold; }
            a:hover { text-decoration: underline; }
            .container { background-color: white; padding: 20px 40px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); display: inline-block; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>API is Running!</h1>
            <p>Welcome to the Simple CRUD API.</p>
            <p>To view the items, visit: <a href="/items" target="_blank">/items</a></p>
            <p>Remember to use the <code>test_api_complex.py</code> script for full functionality!</p>
        </div>
    </body>
    </html>
    """

# --- GET all items ---
# This endpoint handles GET requests to /items and returns the full list of items.
@app.route('/items', methods=['GET'])
def get_items():
    """
    Retrieves and returns the full list of items.
    """
    return jsonify({"items": items})

# --- GET a single item by ID ---
# This endpoint takes an integer 'item_id' from the URL.
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """
    Retrieves a single item by its ID. Returns a 404 error if not found.
    """
    # Use a generator expression to find the item efficiently.
    item = next((item for item in items if item["id"] == item_id), None)
    
    if item is None:
        # If the item is not found, we use 'abort' to return a 404 Not Found error.
        abort(404, description=f"Item with ID {item_id} not found.")
    
    return jsonify({"item": item})

# --- POST (Create) a new item ---
# This endpoint adds a new item to our list.
@app.route('/items', methods=['POST'])
def create_item():
    """
    Creates a new item. Expects a JSON payload with 'name', 'price', and 'quantity'.
    """
    global next_id
    
    # Check if the request body is valid JSON and contains the required keys.
    if not request.json or 'name' not in request.json or 'price' not in request.json or 'quantity' not in request.json:
        abort(400, description="Missing required fields (name, price, quantity).")
        
    new_item = {
        'id': next_id,
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': request.json['quantity']
    }
    
    items.append(new_item)
    next_id += 1
    
    # Return the newly created item and a 201 status code (Created).
    return jsonify({"message": "Item created successfully.", "item": new_item}), 201

# --- PUT (Update) an existing item ---
# This endpoint updates an item based on its ID.
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """
    Updates an existing item by its ID. Returns a 404 if not found.
    """
    # Find the item to update.
    item_to_update = next((item for item in items if item["id"] == item_id), None)
    
    if item_to_update is None:
        abort(404, description=f"Item with ID {item_id} not found.")
        
    # Check for a valid JSON request body.
    if not request.json:
        abort(400, description="Invalid JSON request body.")
    
    # Update the item with new data from the request.
    item_to_update['name'] = request.json.get('name', item_to_update['name'])
    item_to_update['price'] = request.json.get('price', item_to_update['price'])
    item_to_update['quantity'] = request.json.get('quantity', item_to_update['quantity'])
    
    return jsonify({"message": "Item updated successfully.", "item": item_to_update})

# --- DELETE an item ---
# This endpoint removes an item based on its ID.
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """
    Deletes an item by its ID. Returns a 404 if not found.
    """
    # Find the index of the item to delete.
    item_index = next((i for i, item in enumerate(items) if item["id"] == item_id), None)
    
    if item_index is None:
        abort(404, description=f"Item with ID {item_id} not found.")
        
    del items[item_index]
    
    return jsonify({"message": "Item deleted successfully."})

# Run the application.
if __name__ == '__main__':
    app.run(debug=True)
