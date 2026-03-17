from fastapi import Request
from fastapi.responses import JSONResponse


class AppException(Exception):
    def __init__(self, status_code: int, detail: str):
        self.status_code = status_code
        self.detail = detail


class NotFoundError(AppException):
    def __init__(self, resource: str):
        super().__init__(404, f"{resource} not found")


class ConflictError(AppException):
    def __init__(self, detail: str):
        super().__init__(409, detail)


class ValidationError(AppException):
    def __init__(self, detail: str):
        super().__init__(422, detail)


class ForbiddenError(AppException):
    def __init__(self, detail: str = "Action not permitted"):
        super().__init__(403, detail)


async def app_exception_handler(request: Request, exc: AppException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
