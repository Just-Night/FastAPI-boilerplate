from settings import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession


db_string = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'.format(
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    db_name=settings.DB_NAME
)

engine = create_engine(db_string, echo=False)

if settings.ASYNC:
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
