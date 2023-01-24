from typing import Any, Dict, Optional, Union  # noqa
from fastapi import HTTPException , status # noqa

from sqlalchemy.orm import Session

from apps.user import model
from apps.auth.utils import get_hashed_password


class Crud:
    def __init__(self) -> None:
        self.User = model.User

    def _create_user(self, db: Session, *, obj_in):
        create_data = obj_in.dict()
        create_data.pop("password")
        db_obj = self.User(**create_data)
        db_obj.hashed_password = get_hashed_password(obj_in.password)
        db.add(db_obj)
        db.commit()

        return db_obj

    def check_user_create(self, db: Session, user_in):
        user_query: model.User = db.query(self.User).filter(model.User.login == str(user_in.login)).first()
        if user_query:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The login already exists!",
            )


UserCrud = Crud()
