from fastapi import FastAPI
from app.api.endpoints import orders

app = FastAPI()

app.include_router(orders.router, prefix="/api")