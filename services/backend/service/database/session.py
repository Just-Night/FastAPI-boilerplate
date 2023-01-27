from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Generator
from settings import config


db_string = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'.format(  # noqa
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=config.DB_PORT,
    db_name=config.DB_NAME
)

engine = create_engine(db_string, echo=False)
if config.ASYNC:
    async_session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False)

    db_session: AsyncSession = async_session()

    async def get_db() -> Generator:
        try:
            yield db_session
        finally:
            db_session.close()

else:
    session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

    db_session: sessionmaker = session()

    def get_db() -> Generator:
        yield db_session
