from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# TODO: Task 1 — Add a GET endpoint at "/" that returns a welcome message
@app.get("/")
def read_root():
    pass  # Replace with your implementation


# TODO: Task 2 — Add a GET endpoint at "/items/{item_id}"
# Accept an optional query parameter "q" and include it in the response when provided
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    pass  # Replace with your implementation


# TODO: Task 3 — Define a Pydantic model with at least three fields
# Then add a POST endpoint at "/items/" that accepts the model as the request body
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool


@app.post("/items/")
def create_item(item: Item):
    pass  # Replace with your implementation
