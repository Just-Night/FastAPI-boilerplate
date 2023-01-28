from fastapi import (  # noqa
    APIRouter,
    Depends,
    status
    )
from typing import List

from apps.utils import get_current_user
from database import get_db
from crud import UserCRUD
from . import schemas

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.get("/me", response_model=schemas.User, status_code=status.HTTP_200_OK)
def read_users_me(current_user=Depends(get_current_user)):
    """
    Fetch the current logged in user.
    """

    return current_user


@router.get('/list', response_model=List[schemas.User], status_code=status.HTTP_200_OK)
def get_users_list(skip: int = 0, limit:int = 100, db=Depends(get_db), curent_user=Depends(get_current_user)):
    return UserCRUD.get_user_list(db, limit, skip)


@router.get('/{login}', response_model=schemas.User, status_code=status.HTTP_200_OK)
def get_user_by_login(login: str, db=Depends(get_db), curent_user=Depends(get_current_user)):
    query = UserCRUD.get_user(db, login)
    if query is None:
        return "Not found"
    return query
