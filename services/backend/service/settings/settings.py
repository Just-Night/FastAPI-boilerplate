import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_NAME = os.environ.get('PROJECT_NAME', 'Boilerplate')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG')))

# SWAGGER URL
DOCKS_URL = os.environ.get('DOCKS_URL', None)
REDOC_URL = os.environ.get('REDOC_URL', None)

ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get('ALLOWED_HOSTS', '*').split(','),
    )
)

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
