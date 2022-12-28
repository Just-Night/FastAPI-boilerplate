import uuid
from sqlalchemy import(  # noqa: disable=F401
    Table,
    Column,
)
from sqlalchemy.dialects.postgresql import UUID  # noqa:disable=F401

from sqlalchemy.ext.declarative import declarative_base, declared_attr

BASE = declarative_base()


# class BASE_MODEL(BASE):
#     __abstract__ = True

#     @declared_attr
#     def __tablename__(cls) -> str:
#         return f"{cls.__name__.lower()}s"

#     id = Column(
#             UUID(as_uuid=True),
#             primary_key=True,
#             unique=True,
#             default=uuid.uuid4
#         )
