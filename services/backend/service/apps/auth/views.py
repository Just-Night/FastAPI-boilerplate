from fastapi import (  # noqa
    APIRouter,
    Depends,
    HTTPException,
    status
    )

from database import get_db

from . import schemas
from .utils import (
    authenticate,
    create_access_token,
    create_refresh_token
    )

from crud import UserCRUD

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


@router.post("/signin", status_code=status.HTTP_202_ACCEPTED)
async def user_signin(auth: schemas.OAuth2, db=Depends(get_db)):
    """
    Get the JWT for a user with data from OAuth2 request form body.
    """

    user = authenticate(login=auth.login, password=auth.password, db=db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {
        "access_token": create_access_token(user.id),
        "refresh_token": create_refresh_token(user.id),
    }


@router.post("/signup", status_code=status.HTTP_201_CREATED)
def create_user_signup(user_in: schemas.OAuth2, db=Depends(get_db)):
    """
    Create new user without the need to be logged in.
    """

    UserCRUD.check_user_login(db, user_in)
    UserCRUD.create_user(db, obj_in=user_in)

    return {"message": "Successful create!"}
