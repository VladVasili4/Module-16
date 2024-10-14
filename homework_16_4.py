from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List
app = FastAPI()

users = []

class User(BaseModel):
    id: int = 0
    username: str = 'Master'
    age: int = 99

@app.get("/users")
def get_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
def create_user(username: str, age: int, user: User) -> User:
    user.id = len(users)+1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{id}/{username}/{age}')
def update_user(id: int, username: str, age: int, user: User = Body()) -> User:
    try:
        edit_user = users[id-1]
        edit_user.username = username
        edit_user.age = age
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete('/user/{id}')
def delete_user(id: int, user: User ) -> User:
    try:
        users.pop(id-1)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


# python -m uvicorn main:app
