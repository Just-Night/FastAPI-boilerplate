import sqlalchemy as models
from core.db import BaseModel


class Example(BaseModel):
    name = models.Column(
        models.String(length=25),
    )
    text = models.Column(
        models.Text(length=5000)
    )

    class Config:
        orm_mode = True
