from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: str, age: str) -> str:
    user_id = str(int(max(users, key=int))+1)
    users[user_id] = 'Имя: username, возраст: age'
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_message(user_id: str, username: str, age: str) -> str:
    users[user_id] = 'Имя: username, возраст: age'
    return f"The user {user_id} has been registered"

@app.delete('/user/{user_id}')
async def delete_message(user_id: str) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted"'







# python -m uvicorn main:app