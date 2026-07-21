from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="User Service")

# In-memory database
users = {}

class User(BaseModel):
    id: int
    name: str
    email: str

@app.get("/")
def home():
    return {"message": "Welcome to User Service"}

@app.get("/health")
def health():
    return {"status": "UP"}

@app.get("/users")
def get_users():
    return list(users.values())

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.post("/users")
def create_user(user: User):
    if user.id in users:
        raise HTTPException(status_code=400, detail="User already exists")

    users[user.id] = user.dict()
    return {
        "message": "User created",
        "user": users[user.id]
    }

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    users[user_id] = user.dict()
    return {
        "message": "User updated",
        "user": users[user_id]
    }

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    del users[user_id]

    return {
        "message": "User deleted"
    }
