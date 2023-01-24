from sqlalchemy.orm.session import Session
from typing import Optional, Union, Any

from jose import jwt
from passlib.context import CryptContext

from datetime import datetime

from settings import config
from apps import models


PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


# security
def get_hashed_password(password: str) -> str:
    return PWD_CONTEXT.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return PWD_CONTEXT.verify(password, hashed_pass)


# auth
def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + config.ACCESS_TOKEN_EXPIRE

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, config.JWT_SECRET_KEY, config.ALGORITHM)
    return encoded_jwt


def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        expires_delta = datetime.utcnow() + expires_delta
    else:
        expires_delta = datetime.utcnow() + config.REFRESH_TOKEN_EXPIRE

    to_encode = {"exp": expires_delta, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, config.JWT_SECRET_KEY, config.ALGORITHM)
    return encoded_jwt


def authenticate(login: str, password: str, db: Session) -> Optional[models.User]:
    user: models.User = db.query(models.User).filter(models.User.login == login).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
