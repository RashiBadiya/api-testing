# test_api_complex.py
# This script provides a comprehensive test suite for the app_complex.py API,
# covering all CRUD (Create, Read, Update, Delete) operations.

import requests
import json
import time

# Define the base URL of the API.
BASE_URL = "http://127.0.0.1:5000"

# A variable to hold the ID of the item we create during the test.
created_item_id = None

def run_tests():
    """
    Orchestrates the entire test suite in a logical order.
    """
    print("--- Starting Comprehensive API Test Suite ---")
    
    try:
        # Step 1: Test the 'GET all items' endpoint.
        test_get_all_items()
        
        # Step 2: Test the 'POST (Create)' endpoint.
        test_create_item()
        
        # We need the ID of the created item for subsequent tests.
        if created_item_id:
            # Step 3: Test the 'GET single item' endpoint using the new item's ID.
            test_get_single_item(created_item_id)
            
            # Step 4: Test the 'PUT (Update)' endpoint.
            test_update_item(created_item_id)
            
            # Step 5: Test the 'DELETE' endpoint.
            test_delete_item(created_item_id)
            
            # Step 6: Verify the item is truly deleted by trying to GET it.
            test_get_deleted_item(created_item_id)
        
    except requests.exceptions.ConnectionError:
        print("\n[!] Error: Could not connect to the API. Make sure 'app_complex.py' is running.")
        print("    Run 'python app_complex.py' in a separate terminal and then try again.")

def test_get_all_items():
    """Tests the GET /items endpoint."""
    print("\n[+] Testing GET /items (get all items)...")
    response = requests.get(f"{BASE_URL}/items")
    print(f"    Status Code: {response.status_code}")
    print(f"    Response Body: {response.json()}")
    assert response.status_code == 200, "GET all items failed."
    print("    Test passed: Successfully retrieved all items.")

def test_create_item():
    """Tests the POST /items endpoint."""
    global created_item_id
    print("\n[+] Testing POST /items (create new item)...")
    new_item_data = {"name": "Test Item", "price": 9.99, "quantity": 100}
    response = requests.post(f"{BASE_URL}/items", json=new_item_data)
    
    print(f"    Status Code: {response.status_code}")
    print(f"    Response Body: {response.json()}")
    assert response.status_code == 201, "POST create item failed."
    assert "item" in response.json(), "Response did not contain the new item."
    
    # Extract the ID of the newly created item.
    created_item_id = response.json().get('item', {}).get('id')
    assert created_item_id is not None, "Could not get ID of created item."
    
    print(f"    Test passed: Item created with ID: {created_item_id}")

def test_get_single_item(item_id):
    """Tests the GET /items/<id> endpoint."""
    print(f"\n[+] Testing GET /items/{item_id} (get single item)...")
    response = requests.get(f"{BASE_URL}/items/{item_id}")
    print(f"    Status Code: {response.status_code}")
    print(f"    Response Body: {response.json()}")
    assert response.status_code == 200, "GET single item failed."
    assert response.json().get('item', {}).get('id') == item_id, "Retrieved item ID does not match."
    print("    Test passed: Successfully retrieved the created item.")

def test_update_item(item_id):
    """Tests the PUT /items/<id> endpoint."""
    print(f"\n[+] Testing PUT /items/{item_id} (update item)...")
    update_data = {"name": "Updated Test Item", "price": 12.50}
    response = requests.put(f"{BASE_URL}/items/{item_id}", json=update_data)
    print(f"    Status Code: {response.status_code}")
    print(f"    Response Body: {response.json()}")
    assert response.status_code == 200, "PUT update item failed."
    assert response.json().get('item', {}).get('name') == "Updated Test Item", "Item name not updated."
    print("    Test passed: Item updated successfully.")

def test_delete_item(item_id):
    """Tests the DELETE /items/<id> endpoint."""
    print(f"\n[+] Testing DELETE /items/{item_id} (delete item)...")
    response = requests.delete(f"{BASE_URL}/items/{item_id}")
    print(f"    Status Code: {response.status_code}")
    print(f"    Response Body: {response.json()}")
    assert response.status_code == 200, "DELETE item failed."
    print("    Test passed: Item deleted successfully.")

def test_get_deleted_item(item_id):
    """Verifies that a deleted item cannot be retrieved."""
    print(f"\n[+] Verifying GET /items/{item_id} (deleted item)...")
    response = requests.get(f"{BASE_URL}/items/{item_id}")
    print(f"    Status Code: {response.status_code}")
    assert response.status_code == 404, "Deleted item still exists."
    print("    Test passed: Item is confirmed to be deleted (404 Not Found).")

if __name__ == '__main__':
    run_tests()
