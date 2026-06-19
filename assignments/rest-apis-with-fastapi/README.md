# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build REST APIs using Python's FastAPI framework. By the end of this assignment, you will create a fully working API with multiple endpoints, path and query parameters, and request body validation using Pydantic models.

## 📝 Tasks

### 🛠️	Create a FastAPI App and Your First Endpoint

#### Description
Set up a FastAPI application and define a basic GET endpoint that returns a JSON response. Run the app locally to confirm it works.

#### Requirements
Completed program should:

- Import FastAPI and create an app instance.
- Define a GET endpoint at `/` that returns a JSON welcome message.
- Run successfully with `uvicorn` and respond at `http://127.0.0.1:8000/`.

### 🛠️	Add Endpoints with Path and Query Parameters

#### Description
Extend the API with endpoints that accept dynamic path parameters and optional query parameters to filter or customise the response.

#### Requirements
Completed program should:

- Define a GET endpoint at `/items/{item_id}` that returns the item ID in the response.
- Accept an optional query parameter `q` on the `/items/{item_id}` endpoint and include it in the response when provided.
- Return appropriate JSON responses for both cases (with and without `q`).

### 🛠️	Validate Request Bodies with Pydantic Models

#### Description
Add a POST endpoint that accepts a JSON request body and validates it using a Pydantic model.

#### Requirements
Completed program should:

- Define a Pydantic `BaseModel` with at least three fields (for example: `name`, `price`, and `in_stock`).
- Define a POST endpoint at `/items/` that accepts the model as the request body.
- Return the received item data as a JSON response, confirming successful validation.
- Reject invalid request bodies automatically (missing required fields or wrong types).
