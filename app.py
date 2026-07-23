from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

from auth import verify_token, login_router

app = FastAPI(title="User Service")

# Register the /login route from auth.py
app.include_router(login_router)

# In-memory database
users = {
    1: {"id": 1, "name": "chandra Sharma", "email": "chandra@piet.com"},
    2: {"id": 2, "name": "ram Mehta", "email": "ram@piet.com"},
}



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


@app.get("/usersJwt")
def get_users_jwt(user: str = Depends(verify_token)):
    return {
        "logged_in_user": user,
        "users": list(users.values())
    }
