from fastapi import (  # noqa
    APIRouter,
    Depends,
    status
    )

from apps.utils import get_current_user
from . import schemas

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.get("/me", response_model=schemas.User, status_code=status.HTTP_200_OK)
def read_users_me(current_user=Depends(get_current_user)):
    """
    Fetch the current logged in user.
    """

    return current_user
