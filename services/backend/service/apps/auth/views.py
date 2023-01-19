from fastapi import (  # noqa
    APIRouter,
    Depends,
    Form,
    HTTPException,
    status
    )
# from fastapi.security import OAuth2PasswordRequestForm
from typing import Any

from .schemas import (
    User,
    OAuth2Password
)
from .utils import authenticate, create_access_token
from database import Session

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post("/signin")
async def login(auth: OAuth2Password) -> Any:
    """
    Get the JWT for a user with data from OAuth2 request form body.
    """
    user = await authenticate(login=auth.login, password=auth.password, db=Session)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {
        "access_token": create_access_token(sub=user.id),
        "token_type": "bearer",
    }


# @router.post("/signup", response_model=User, status_code=201)  # 1
# def create_user_signup(
#     user_in: user.UserCreate  # 3
# ) -> Any:
#     """
#     Create new user without the need to be logged in.
#     """

#     user_query: User = db.query(User).filter(User.email == user_in.email or User.nickname == user_in.nickname).first()
#     if user_query.email == user_in.email:
#         raise HTTPException(  # 5
#             status_code=400,
#             detail="The email already exists!",
#         )
#     if user_query.nickname == user_in.nickname:
#         raise HTTPException(
#             status_code=400,
#             detail="This nickname already exists!"
#         )

#     user = crud.user.create(db=db, obj_in=user_in)  # 6

#     return user
