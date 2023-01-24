from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from jose import JWTError, jwt
from passlib.context import CryptContext


from settings import config
from apps import models
from .auth import schemas
from database import db_session


PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/signin")

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


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(db_session)):  # noqa
    try:
        payload = jwt.decode(
            token,
            config.JWT_SECRET_KEY,
            algorithms=[config.ALGORITHM],
            options={"verify_aud": False},
        )
        uuid: str = payload.get("sub")
        if uuid is None:
            raise credentials_exception_404_NOT_FOUND
        token_data = schemas.TokenData(uuid=uuid)
    except JWTError:
        raise credentials_exception_UNAUTHORIZED

    user = db.query(models.User).filter(models.User.id == token_data.uuid).first()
    if user is None:
        raise credentials_exception_UNAUTHORIZED
    return user
