from typing import Union, List, Optional  # noqa
from pydantic import BaseModel, SecretStr  # noqa
from uuid import UUID


class Base(BaseModel):
    id: Optional[UUID]

    class Config:
        orm_mode = True


class OAuth2(BaseModel):
    login: Optional[str] = None
    password: Optional[str] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    uuid: Optional[UUID] = None
