from pydantic import BaseModel

from typing import List, Optional  # noqa: disable=F401
from uuid import UUID


class Base(BaseModel):
    id: Optional[UUID]

    class Config:
        orm_mode = True


class User(Base):
    login: Optional[str]
    is_staff: Optional[bool]
    is_superuser: Optional[bool]
