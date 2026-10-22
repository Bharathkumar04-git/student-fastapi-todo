from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="To-Do API")

# Mock database
todos = []

class TodoItem(BaseModel):
    id: int
    task: str
    completed: bool = False

@app.get("/")
def home():
    return {"message": "To-Do Tracker API is online!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/todos", response_model=List[TodoItem])
def get_todos():
    return todos

@app.post("/todos", response_model=TodoItem)
def add_todo(item: TodoItem):
    todos.append(item)
    return item
