from typing import Union, List, Optional  # noqa
from pydantic import BaseModel, Field  # noqa


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    login: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None


class OAuth2Password(BaseModel):
    login: Optional[str]
    password: Optional[str]


class UserInDB(User):
    hashed_password: str
