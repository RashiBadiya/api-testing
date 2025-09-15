# API testing

This project contains a simple yet comprehensive CRUD (Create, Read, Update, Delete) API built with Flask. It manages an in-memory collection of items.

## Files

- `api.py`: The main Flask application. It provides endpoints to manage a list of items.
- `test.py`: A test script that uses the `requests` library to perform a full test suite on the API, covering all CRUD operations.

## How to Run

1.  **Start the API:**
    Open a terminal and run the Flask application:
    ```bash
    python api.py
    ```
    The API will be running at `http://127.0.0.1:5000`. You can visit this URL in your browser to see a welcome message.

2.  **Run the Tests:**
    Open a second terminal and run the test script:
    ```bash
    python test.py
    ```
    This script will call each endpoint and verify that the API is working correctly.

## How It Works

The project consists of two main files: a web API (`api.py`) and a script to test that API (`test.py`).

### 1. The API (`api.py`)

This file uses the **Flask** web framework to create a simple REST API. Think of it as a small web server that responds to specific URLs with data.

*   **In-Memory "Database"**: It uses a simple Python list called `items` to store data. This acts as a temporary database that resets every time you restart the server.
*   **CRUD Operations**: The API provides endpoints for the four basic functions of data management:
    *   **Create**: `POST /items` — Allows you to add a new item to the list.
    *   **Read**:
        *   `GET /items` — Retrieves the entire list of items.
        *   `GET /items/<id>` — Retrieves a single item by its unique ID.
    *   **Update**: `PUT /items/<id>` — Allows you to modify an existing item.
    *   **Delete**: `DELETE /items/<id>` — Removes an item from the list.
*   **Running the Server**: When you run `python api.py`, it starts a local web server (usually at `http://127.0.0.1:5000`), making the API accessible.

### 2. The Test Script (`test.py`)

This file acts as a client that automatically tests every part of your API to make sure it's working correctly.

*   **Making Requests**: It uses the `requests` library, which is a standard way to send HTTP requests in Python (the same kind of requests your web browser sends).
*   **Test Suite**: The script defines a series of functions, each designed to test one specific API endpoint.
*   **Logical Flow**: The tests run in a logical order to simulate a real user's actions:
    1.  It first **creates** a new item.
    2.  Then, it **reads** that specific item to make sure it was created correctly.
    3.  Next, it **updates** the item with new data.
    4.  After that, it **deletes** the item.
    5.  Finally, it tries to read the deleted item again to confirm it's truly gone.
*   **Assertions**: It uses `assert` statements to automatically check if the API's responses are what's expected. For example, it checks if creating an item returns a `201 Created` status code or if deleting an item makes it inaccessible (`404 Not Found`).

In short, `api.py` **is** the service, and `test.py` **is the quality check** that ensures the service does its job correctly.
