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
def create_user(username: str, age: int):
    user_id = len(users) + 1
    user = User(id=user_id, username=username, age=age)
    users.append(user)
    return user


@app.put('/user/{id}/{username}/{age}')
async def update_user(id: int, username: str, age: int):
    try:
        edit_user = users[id-1]
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

@app.delete('/user/{id}')
def delete_user(id: int): 
    try:
        user = User()
        users.pop(id-1)
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


# python -m uvicorn main:app
