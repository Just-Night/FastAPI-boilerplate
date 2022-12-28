from main import BASE
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


class User(BASE):
    __tablename__ = "users"

    login = Column(String, unique=True)
    password = Column(String, nullable=True)
