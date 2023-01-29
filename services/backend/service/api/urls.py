from fastapi import APIRouter
from api.v1 import urls

api_router: APIRouter = APIRouter(
    prefix='/api',
)

api_router.include_router(urls.router)
