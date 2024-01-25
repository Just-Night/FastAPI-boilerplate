from fastapi import APIRouter, Request, Response, status
from pydantic_async_validation.fastapi import ensure_request_validation_errors

from apps.example.services import ExampleService
from apps.example.schemas import ExampleRequestSchemaInput
from apps.models import Example


router = APIRouter(
    prefix='/example',
    tags=['Example']
)


@router.post('/create/')
async def create(request: Request, create_input: ExampleRequestSchemaInput):
    language = str(request.state.language)
    with ensure_request_validation_errors():
        await create_input.model_async_validate()
    example: Example = await ExampleService.create(**create_input.model_dump())
    return Response(f'{example}\n {language}', status.HTTP_201_CREATED)
