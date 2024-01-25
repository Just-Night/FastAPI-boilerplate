from pydantic import BaseModel
from pydantic_async_validation import (AsyncValidationModelMixin,
                                       async_field_validator)


class ExampleRequestSchemaInput(AsyncValidationModelMixin, BaseModel):
    name: str
    text: str

    @async_field_validator('name', mode='before')
    async def name_validator(self, value: str):
        return value

    @async_field_validator('text', mode='before')
    async def text_validator(self, value):
        return value
