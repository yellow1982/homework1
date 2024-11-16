from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
def get_all_users() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
def add_user(user: User, username: str, age: int):
    if not users:
        user.id = 1
    else:
        user.id = len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: int, username: str, age: int):
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
def delete_user(user_id: int):
    try:
        deleted_user = users.pop(user_id-1)
        return deleted_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")
