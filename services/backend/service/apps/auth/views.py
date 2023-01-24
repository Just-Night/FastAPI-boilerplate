from fastapi import (  # noqa
    APIRouter,
    Depends,
    Form,
    HTTPException,
    status
    )

from typing import Any
from database import Session

from . import schemas
from .utils import (
    authenticate,
    create_access_token,
    create_refresh_token
    )

from crud import UserCrud

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post("/signin", status_code=status.HTTP_202_ACCEPTED)
async def user_signin(auth: schemas.OAuth2) -> Any:
    """
    Get the JWT for a user with data from OAuth2 request form body.
    """

    user = authenticate(login=auth.login, password=auth.password, db=Session)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {
        "access_token": create_access_token(user.id),
        "refresh_token": create_refresh_token(user.id),
    }


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def create_user_signup(user_in: schemas.OAuth2) -> Any:
    """
    Create new user without the need to be logged in.
    """

    UserCrud.check_user_create(db=Session, user_in=user_in)
    UserCrud._create_user(db=Session, obj_in=user_in)

    return {"message": "Successful create!"}
