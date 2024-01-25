import os
from pathlib import Path
from datetime import timedelta


class Config:
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent
    LOCALES_PATH = f'{BASE_DIR}/locales/'
    SUPPORTED_LANGUAGES = ['en', 'uk']
    # SET PROJECT NAME
    PROJECT_NAME = os.environ.get('PROJECT_NAME', 'Boilerplate')
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ.get('SECRET_KEY', 'SET_SECRET_KEY')
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = bool(int(os.environ.get('DEBUG'), 0))
    # SWAGGER URL
    DOCKS_URL = os.environ.get('DOCKS_URL', None)
    REDOC_URL = os.environ.get('REDOC_URL', None)
    # Domain
    DOMAIN = os.environ.get('DOMAIN', 'localhost')
    # HOST
    ALLOWED_HOSTS = []
    ALLOWED_HOSTS.extend(
        filter(
            None,
            os.environ.get('ALLOWED_HOSTS', '*').split(','),
        )
    )
    # CORS
    CORS_ALLOWED_ORIGINS = []
    CORS_ALLOWED_ORIGINS.extend(
        filter(
            None,
            os.environ.get('CORS_ALLOWED_ORIGINS', '*').split(','),
        )
    )
    CORS_ALLOW_METHODS = []
    CORS_ALLOW_METHODS.extend(
        filter(
            None,
            os.environ.get('CORS_ALLOW_METHODS', '*').split(','),
        )
    )
    # PGSQL
    PG_NAME = os.environ.get('POSTGRES_DB')
    PG_USER = os.environ.get('POSTGRES_USER')
    PG_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    PG_HOST = os.environ.get('POSTGRES_HOST')
    PG_PORT = os.environ.get('POSTGRES_PORT')
    PG_URL = 'postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}'.format(
        user=PG_USER,
        password=PG_PASSWORD,
        host=PG_HOST,
        port=PG_PORT,
        db_name=PG_NAME
    )

    # Redis
    REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    REDIS_URL = 'redis://{host}:{port}'.format(
        host=REDIS_HOST,
        port=REDIS_PORT
    )

    # JWT
    ACCESS_TOKEN_EXPIRE = timedelta(minutes=5)
    REFRESH_TOKEN_EXPIRE = timedelta(days=7)
    ALGORITHM = "HS256"
    JWT_SECRET_KEY = SECRET_KEY

    # Sentry
    USE_SENTRY = bool(int(os.environ.get('USE_SENTRY')))
    SENTRY_DSN = os.environ.get('SENTRY_DSN')
    SENTRY_TRACE_SAMPLE_RATE = float(os.environ.get('SENTRY_TRACE_SAMPLE_RATE', 1.0))
    SENTRY_PROFILE_SAMPLE_RATE = float(os.environ.get('SENTRY_PROFILE_SAMPLE_RATE', 1.0))
