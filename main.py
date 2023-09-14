from typing import List, Optional

from fastapi import FastAPI, HTTPException
from fastapi import status
from models import User
app = FastAPI()

users = {
    1: {
        'id': 1,
        'name': 'user 001',
        'email': 'email001@email.com'
    },
    2: {
        'id': 2,
        'name': 'user 002',
        'email': 'email002@email.com'
    }
}


@app.get('/')
async def get_users():
    return users


@app.get('/{user_id}')
async def get_user(user_id: int):
    try:
        user = users[user_id]
        user.update({'id': user_id})
        return user
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )


@app.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    next_id: int = len(users) + 1
    users[next_id] = user
    del user.id
    return user


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=8000,
        reload=True
    )
