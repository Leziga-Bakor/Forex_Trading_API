from pydantic import BaseModel
from app.api.models.enums import OrderStatus

class OrderInput(BaseModel):
    stocks: str
    quantity: float

class OrderOutput(BaseModel):
    id: str
    stocks: str
    quantity: float
    status: OrderStatus