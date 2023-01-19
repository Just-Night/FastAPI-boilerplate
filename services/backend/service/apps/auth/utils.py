from fastapi.security import OAuth2PasswordBearer  # , OAuth2PasswordRequestForm
from fastapi import HTTPException, status
from typing import Optional, Union, Any
from sqlalchemy.orm.session import Session

from jose import jwt
from passlib.context import CryptContext

from datetime import datetime

from settings import settings
from apps.models import User
# from .schemas import User as User_


PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

credentials_exception_UNAUTHORIZED = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
)

credentials_exception_404_NOT_FOUND = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Not found user",
        headers={"WWW-Authenticate": "Bearer"}
)


# security
async def get_hashed_password(password: str) -> str:
    return PWD_CONTEXT.hash(password)


async def verify_password(password: str, hashed_pass: str) -> bool:
    return PWD_CONTEXT.verify(password, hashed_pass)


# auth
async def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + settings.ACCESS_TOKEN_EXPIRE

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt


async def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + settings.REFRESH_TOKEN_EXPIRE

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt


async def authenticate(login: str, password: str, db: Session) -> Optional[User]:
    user: User = db.query(User).filter(User.login == login).first()
    if not user:
        return None
    if not await verify_password(password, user.hashed_password):
        return None
    return user
