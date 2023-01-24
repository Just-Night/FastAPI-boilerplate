from datetime import datetime
from fastapi import APIRouter
from settings import settings

router = APIRouter(
    prefix='/default_app',
    tags=["default app"]
)


@router.get("/test")
def get():
    return datetime.utcnow() + settings.REFRESH_TOKEN_EXPIRE
