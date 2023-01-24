from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
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

    Session: AsyncSession = async_session()

else:
    session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

    Session: sessionmaker = session()


def db_session() -> sessionmaker:
    yield Session


async def db_session_sync() -> sessionmaker:
    yield Session
