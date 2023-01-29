from typing import Generic, Type, TypeVar

from database.model import BASE_MODEL

ModelType = TypeVar("ModelType", bound=BASE_MODEL)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model
