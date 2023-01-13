from fastapi import APIRouter


router = APIRouter(
    prefix='',
)


@router.get("/defauls")
def env():
    return "default"
