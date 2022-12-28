from settings import settings
from database import BASE
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_string = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'.format(
    user=settings.DB_USER,
    password=settings.DB_PASSWORD,
    host=settings.DB_HOST,
    port=settings.DB_PORT,
    db_name=settings.DB_NAME
)

engine = create_engine(db_string, echo=False)

session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Session = session()
