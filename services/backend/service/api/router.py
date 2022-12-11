from fastapi import APIRouter, Depends, HTTPException  # noqa
import settings.settings as st

routers: APIRouter = APIRouter(
    prefix='/test',
    tags=['test']
)

@routers.get("/test")
async def test():
    return st.REDOC_URL
