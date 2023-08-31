from fastapi import FastAPI, WebSocket
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.api.endpoints.errors import error_400
from app.api.endpoints import orders
from app.websocket import websocket_manager

app = FastAPI()

app.include_router(orders.router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    message = "Invalid Input"
    return JSONResponse(content=error_400.model_dump(), status_code=400)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket_manager.connect(websocket)