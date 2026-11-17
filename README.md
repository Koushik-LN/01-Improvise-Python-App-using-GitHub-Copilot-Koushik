
# Text Token API

## Overview

Text Token API is a Python-based REST API developed using FastAPI.

The application accepts text input, splits the text into tokens, and generates a checksum.

This application is part of the GitHub Copilot hands-on exercise to demonstrate AI-assisted Python development.

## Technologies Used

- Python 3
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- HTTPX
- GitHub Copilot

## Features

1. Personalized welcome message.
2. REST API endpoint for processing text.
3. Token generation using whitespace splitting.
4. Checksum calculation using Unicode character values.
5. JSON request validation using Pydantic.
6. Automated API testing using pytest.

## Project Structure

```text
project/
├── main.py
├── test_main.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3 installed
- pip package manager
- GitHub Codespaces or a local Python environment

## Installation

### Step 1: Open the project directory

Open the terminal in the folder containing main.py.

### Step 2: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 3: Start the FastAPI application

```bash
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The application runs on port 8000.

In GitHub Codespaces, open the forwarded URL for port 8000.

## API Endpoints

### 1. Welcome API

Method: GET

Endpoint: /

Example response:

```json
{
  "message": "Welcome Varsha!"
}
```

### 2. Generate Tokens and Checksum

Method: POST

Endpoint: /generate

Request body:

```json
{
  "text": "Hello World"
}
```

Response:

```json
{
  "tokens": ["Hello", "World"],
  "checksum": 1052
}
```

### Explanation

The API performs two operations.

**Token Generation**

The input text is split into words using Python's split() function.

For example:

Input:

```text
Hello World
```

Tokens:

```json
["Hello", "World"]
```

**Checksum Calculation**

The checksum is calculated by adding the Unicode value of each character in the original input text.

```python
checksum = sum(ord(char) for char in request.text)
```

Spaces are included in the checksum calculation.

## API Documentation

FastAPI automatically generates interactive Swagger documentation.

After starting the server, visit:

```text
http://localhost:8000/docs
```

For GitHub Codespaces, use the forwarded port URL with /docs appended.

You can test the POST endpoint using the "Try it out" button.

## Running Automated Tests

The application includes automated tests using pytest and FastAPI TestClient.

Run:

```bash
python -m pytest -v
```

The test suite covers:

- Welcome endpoint
- Successful text processing
- Single-word input
- Multiple spaces
- Empty input
- Missing required field
- Invalid input type
- Unicode text
- Multiple tokenization scenarios

## Error Handling

FastAPI and Pydantic automatically validate incoming JSON requests.

If the required text field is missing or invalid, the API returns HTTP 422 with validation details.

## GitHub Copilot Usage

GitHub Copilot can assist developers with:

- Generating Python code
- Creating FastAPI endpoints
- Adding Pydantic request models
- Writing documentation
- Creating automated tests
- Identifying and fixing coding issues
- Improving code readability

## Conclusion

This project demonstrates how GitHub Copilot can assist developers in enhancing Python applications, generating API endpoints, writing automated tests, and preparing technical documentation.

The application provides token generation and checksum calculation through a simple FastAPI interface.
