from database import BASE_MODEL, DEFAULT_TIME
from sqlalchemy import(  # noqa: disable=F401
    Table,
    Column,
    ForeignKey,
    String,
    Text,
    text,
    Integer,
    BIGINT,
    Boolean,
    DateTime,
    TIMESTAMP,
    ARRAY
    )


class User(BASE_MODEL, DEFAULT_TIME):

    email = Column(String, unique=True)
    password = Column(String, nullable=True)

    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
