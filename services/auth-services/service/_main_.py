import sentry_sdk
from api import api_router
from core import Config
from core.services import (CustomizeLogger, json_validation_exception_handler,
                           set_locale_middleware)
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware


if Config.USE_SENTRY:
    sentry_sdk.init(
        dsn=Config.SENTRY_DSN,
        traces_sample_rate=Config.SENTRY_TRACE_SAMPLE_RATE,
        profiles_sample_rate=Config.SENTRY_PROFILE_SAMPLE_RATE
    )

app = FastAPI(
    title=Config.PROJECT_NAME,
    openapi_url="/openapi.json",
    debug=Config.DEBUG,
    docs_url=Config.DOCKS_URL,
    redoc_url=Config.REDOC_URL,
)

# logger
logger = CustomizeLogger.make_logger(f'{Config.BASE_DIR}/core/services/logging_config.json')

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.CORS_ALLOWED_ORIGINS,
    allow_methods=Config.CORS_ALLOW_METHODS,
    allow_headers=['*'],
    allow_credentials=True
)

# Router include
app.exception_handler(RequestValidationError)(json_validation_exception_handler)
app.middleware("http")(set_locale_middleware)
app.include_router(api_router)
