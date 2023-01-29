from fastapi import HTTPException , status # noqa
from typing import Any, Dict, Optional, Union  # noqa

from sqlalchemy.orm import Session

from crud.base import CRUDBase
from apps.user import model
from apps.auth.utils import get_hashed_password


class CRUDUser(CRUDBase[model.User]):

    def check_user_login(self, db: Session, user):
        user_query = db.query(self.model).filter(self.model.login == user.login).first()
        if user_query:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="The login already exists!",
            )

    def _create_data(self, *, obj_in):
        create_data = obj_in.dict()
        create_data.pop("password")
        return create_data

    def create_user(self, db: Session, *, obj_in):
        db_obj = self.model(**self._create_data(obj_in=obj_in))
        db_obj.hashed_password = get_hashed_password(obj_in.password)
        db.add(db_obj)
        db.commit()

        return db_obj

    def create_superuser(self, db: Session, *, obj_in):
        if db.query(self.model).filter(
                self.model.login == obj_in.login
                ).first():
            return False

        db_obj = self.model(**self._create_data(obj_in=obj_in))
        db_obj.hashed_password = get_hashed_password(obj_in.password)
        db_obj.is_staff = True
        db_obj.is_superuser = True
        db.add(db_obj)
        db.commit()
        return True

    def get_user(self, db: Session, login):
        user_query = db.query(self.model).filter(self.model.login == login).first()
        if user_query is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found!",
            )
        return user_query

    def get_user_list(self, db: Session, limit: int, skip: int):
        return db.query(self.model).order_by(self.model.created_at.desc()).limit(limit).offset(skip).all()

    def update_user(self, db: Session, login, *, edit_data):
        user_query = db.query(self.model).filter(self.model.login == login).first()
        user_query(**edit_data)
        db.commit(user_query)

    def delete_user(self, db: Session, login):
        user_query = db.query(self.model).filter(self.model.login == login).first()
        db.delete(user_query)


UserCRUD = CRUDUser(model.User)
