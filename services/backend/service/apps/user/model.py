from database import BASE_MODEL
from sqlalchemy import(  # noqa: disable=F401
    Table,
    Column,
    ForeignKey,
    String,
    Text,
    Integer,
    BIGINT,
    Boolean,
    DateTime,
    TIMESTAMP,
    ARRAY
    )


class User(BASE_MODEL):

    login = Column(String, unique=True)
    password = Column(String, nullable=True)
