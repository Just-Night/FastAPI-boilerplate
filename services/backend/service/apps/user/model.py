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

    login = Column(String, unique=True)
    hashed_password = Column(String, nullable=False)

    is_staff = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
