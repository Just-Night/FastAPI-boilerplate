from passlib.context import CryptContext
from datetime import datetime
from typing import Union, Any
from jose import jwt
from settings import settings

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def get_hashed_password(password: str) -> str:
    return PWD_CONTEXT.hash(password)


async def verify_password(password: str, hashed_pass: str) -> bool:
    return PWD_CONTEXT.verify(password, hashed_pass)


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
