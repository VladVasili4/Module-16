from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
                        age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples='24')]) -> str:
    user_id = str(int(max(users, key=int))+1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_message(user_id: Annotated[str, Path(description='Enter user_id', example='2')],
                         username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')],
                        age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples='24')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"The user {user_id} has been updated"

@app.delete('/user/{user_id}')
async def delete_message(user_id: Annotated[str, Path(description='Enter user_id for delete. Warning! All data will be destroyed')]) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'


# python -m uvicorn main:app
