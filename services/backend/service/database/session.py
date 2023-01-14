from settings import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


db_string = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db_name}'.format(  # noqa
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=config.DB_PORT,
    db_name=config.DB_NAME
)

engine = create_engine(db_string, echo=False)

session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Session = session()
