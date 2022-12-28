from fastapi import FastAPI, APIRouter, Request, Depends  # noqa
from fastapi.middleware.cors import CORSMiddleware
from api.urls import api_router
from settings import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url="/openapi.json",
    debug=settings.DEBUG,
    docs_url=settings.DOCKS_URL,
    redoc_url=settings.REDOC_URL
)
# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ALLOWED_ORIGINS,
    allow_methods=settings.CORS_ALLOW_METHODS,
    allow_headers=['*'],
    allow_credentials=True
)
# Router include
app.include_router(api_router)
