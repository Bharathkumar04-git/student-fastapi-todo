from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_home_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "To-Do Tracker API is online!"}

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_add_and_get_todo():
    # Test creating a task
    new_todo = {"id": 1, "task": "Learn DevOps Automation", "completed": False}
    post_res = client.post("/todos", json=new_todo)
    assert post_res.status_code == 200
    
    # Test retrieving the task list
    get_res = client.get("/todos")
    assert get_res.status_code == 200
    assert len(get_res.json()) == 1
    assert get_res.json()[0]["task"] == "Learn DevOps Automation"
