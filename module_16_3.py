from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
def get_all_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
def add_user(username: Annotated[str, Path(min_length=5, max_length=20,
                                           description="Enter username", example="UrbanUser")],
             age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]) -> str:
    current_user = str(int(max(users, key=int)) + 1)
    users[current_user] = f'Имя: {username}, возраст: {age}'
    return f"User {current_user} is registered"


@app.put('/user/{user_id}/{username}/{age}')
def update_user(user_id, username: Annotated[str, Path(min_length=5, max_length=20,
                                                  description="Enter username", example="UrbanUser")],
                    age: Annotated[int, Path(ge=18, le=120, description="Enter age", example=24)]):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}')
def delete_user(user_id):
    users.pop(user_id)
    return f"The user {user_id} is deleted"
