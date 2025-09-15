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
