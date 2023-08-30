from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.api.endpoints.errors import error_400
from app.api.endpoints import orders

app = FastAPI()

app.include_router(orders.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    message = "Invalid Input"
    return JSONResponse(content=error_400.model_dump(), status_code=400)
