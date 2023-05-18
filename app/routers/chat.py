from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func

from .. import models, schemas, oauth2
from ..database import get_db
from ..gptapi import openai


router = APIRouter(
    prefix="/chats",
    tags=['Chats']
)


@router.get("/", response_model=List[schemas.ChatOut])
def get_chats(db: Session = Depends(get_db)):
    chats = db.query(models.Chat)
    return chats


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Chat)
def create_chats(message: schemas.ChatCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    ai_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
                "role": "user", 
                "content": f'{message}'
            }
        ]
    )

    completion = ai_response["choices"][0]["message"]["content"]

    new_chat = models.Chat(owner_id=current_user.id, completion=f'{completion}', **message.dict())
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)

    return new_chat