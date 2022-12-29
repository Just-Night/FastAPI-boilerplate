import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# SET PROJECT NAME
PROJECT_NAME = os.environ.get('PROJECT_NAME', 'Boilerplate')
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'SET_SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG'), 0))
ASYNC = bool(int(os.environ.get('ASYNC'), 0))
# SWAGGER URL
DOCKS_URL = os.environ.get('DOCKS_URL', None)
REDOC_URL = os.environ.get('REDOC_URL', None)
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
# DATABASE
DB_NAME = os.environ.get('POSTGRES_DB')
DB_USER = os.environ.get('POSTGRES_USER')
DB_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
# JWT
ACCESS_TOKEN_EXPIRE = timedelta(days=7)
REFRESH_TOKEN_EXPIRE = timedelta(days=30)
ALGORITHM = "HS256"
JWT_SECRET_KEY = SECRET_KEY
