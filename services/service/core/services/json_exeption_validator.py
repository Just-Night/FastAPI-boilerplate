from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


async def json_validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = {}
    for error in exc.errors():
        field = error['loc'][-1]
        if 'ctx' in error and 'reason' in error['ctx']:
            msg = error['ctx']['reason']
        else:
            msg = error['msg']
        if field not in errors:
            errors[field] = []
        errors[field].append(msg)
    return JSONResponse(status_code=400, content=errors)
