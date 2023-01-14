from fastapi import FastAPI, APIRouter, Request, Depends  # noqa
from fastapi.middleware.cors import CORSMiddleware
from api.urls import api_router
from settings import config

app = FastAPI(
    title=config.PROJECT_NAME,
    openapi_url="/openapi.json",
    debug=config.DEBUG,
    docs_url=config.DOCKS_URL,
    redoc_url=config.REDOC_URL
)
# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ALLOWED_ORIGINS,
    allow_methods=config.CORS_ALLOW_METHODS,
    allow_headers=['*'],
    allow_credentials=True
)
# Router include
app.include_router(api_router)
