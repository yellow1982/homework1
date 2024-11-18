from typing import List, Annotated
from fastapi import FastAPI, HTTPException, Path
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
def add_user(username: Annotated[str, Path(min_length=5, max_length=20,
                                           description="Enter username", example="UrbanUser")],
             age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]):
    user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter user ID", example=1)],
                username: Annotated[str, Path(min_length=5, max_length=20,
                                              description="Enter username", example="UrbanTest")],
                age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=50)]):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter user ID", example=1)]):
    for user in users:
        if user.id == user_id:
            deleted_user = user
            users.remove(user)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")
