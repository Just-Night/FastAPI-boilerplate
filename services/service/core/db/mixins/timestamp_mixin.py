from sqlalchemy import Column, DateTime, Integer, func
from sqlalchemy.ext.declarative import declared_attr
from core import unixify_timestamp
from datetime import datetime


class TimestampMixin:
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=func.now(), nullable=False)

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime,
            default=func.now(),
            onupdate=func.now(),
            nullable=False,
        )

    @declared_attr
    def timestamp_created_at(cls):
        return Column(
            Integer,
            default=lambda: unixify_timestamp(datetime.utcnow())
        )

    @declared_attr
    def timestamp_updated_at(cls):
        return Column(
            Integer,
            default=lambda: unixify_timestamp(datetime.utcnow()),
            onupdate=lambda: unixify_timestamp(datetime.utcnow()),
            nullable=True
        )
