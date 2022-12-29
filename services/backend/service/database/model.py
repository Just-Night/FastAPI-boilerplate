import uuid
from sqlalchemy.dialects.postgresql import UUID  # noqa:disable=F401

from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from sqlalchemy import(  # noqa: disable=F401
    Column,
    DateTime,
)


BASE = declarative_base()


class BASE_MODEL(BASE):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id = Column(
            UUID(as_uuid=True),
            primary_key=True,
            unique=True,
            default=uuid.uuid4
        )


class DEFAULT_TIME(object):
    __abstract__ = True

    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, server_default=func.now())
