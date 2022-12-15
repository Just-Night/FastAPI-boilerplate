from typing import List, Optional  # noqa: disable=F401
from uuid import UUID
from pydantic import BaseModel


class Base(BaseModel):
    id: Optional[UUID]

    class Config:
        orm_mode = True
