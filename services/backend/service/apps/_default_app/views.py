from datetime import datetime
from fastapi import APIRouter
from settings import config

router = APIRouter(
    prefix='/default_app',
    tags=["default app"]
)


@router.get("/test")
def get():
    return datetime.utcnow() + config.REFRESH_TOKEN_EXPIRE
