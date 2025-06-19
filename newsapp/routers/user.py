from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models, oauth2
from typing import List
from sqlalchemy.orm import Session

from ..repository import userRepository

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db


@router.post('/signup', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return userRepository.create(request,db)


@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(current_user: schemas.User = Depends(oauth2.get_current_user)):
    return current_user