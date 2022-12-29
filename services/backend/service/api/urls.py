from fastapi import APIRouter
from .v1 import urls
from apps._default_app import views
api_router: APIRouter = APIRouter(
    prefix='/api',
)

api_router.include_router(urls.router)

api_router.include_router(views.router)
