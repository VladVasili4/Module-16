from fastapi import FastAPI, Path, HTTPException, status, Body
# from typing import Annotated
from pydantic import BaseModel
from typing import  List

app = FastAPI()

messages_db = []
class Message(BaseModel):
    id: int = None
    text: str


@app.get('/')
def get_all_messages() -> List(Message):
    return messages_db

# @app.get('/main')
# async def main_() -> dict:
#     return {'message': 'Main Page'}

@app.get(path='/message/{message}')
def get_message(message_id: int) -> Message:
    try:
        return messages_db[message_id]
    except IndexError:
        raise HTTPException(status_code=404, detail='Message Not found')

@app.post('/message')
def create_message(message: Message) -> str:
    message_id = len(messages_db)
    messages_db.append(message)
    return 'Message created'

@app.put('/message/{message_id}')
def put_message(message_id: int, message: str = Body()) -> str:
    try:
        edit_message = messages_db[message_id]
        edit_message.text = message
        return 'Message updated'
    except IndexError:
        raise HTTPException(status_code=404, detail='Message Not found')

@app.delete('/message/{message_id}')
def delete_message(message_id: int) -> str:
    try:
        messages_db.pop(message_id)
        return f'Message ID={message_id} has been deleted'
    except IndexError:
        raise HTTPException(status_code=404, detail='Message Not found')

@app.delete('/')
def clear_all() -> str:
    messages_db.clear()
    return 'All messages deleted'


# В документации по Pydentic должно быть хорошо написано про валидацию
# uvicorn main:app              - запуск сервака