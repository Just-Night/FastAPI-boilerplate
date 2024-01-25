from apps.models import Example
from core.db import Transactional, session


class ExampleService:

    @classmethod
    @Transactional()
    async def create(self, name: str, text: str) -> Example:
        example = Example(name=name, text=text)
        session.add(example)
        await session.commit()
        return example
