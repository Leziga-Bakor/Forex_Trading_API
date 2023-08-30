from pydantic import BaseModel
from app.api.models.enums import OrderStatus

class OrderInput(BaseModel):
    stoks: str
    quantity: float

class OrderOutput(BaseModel):
    id: str
    stoks: str
    quantity: float
    status: OrderStatus