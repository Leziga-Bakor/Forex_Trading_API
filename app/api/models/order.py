from pydantic import BaseModel, validator
from app.api.models.enums import OrderStatus

class OrderInput(BaseModel):
    stoks: str
    quantity: float

    @validator("stoks")
    def validate_stoks(cls, v):
        if not v.strip():  # Check if the input is empty or contains only whitespace
            raise ValueError("stoks must not be empty or contain only whitespace")
        return v

    @validator("quantity")
    def validate_quantity(cls, v):
        if v <= 0: # check if the input is negative
            raise ValueError("quantity must be a positive value")
        return v

class OrderOutput(BaseModel):
    id: str
    stoks: str
    quantity: float
    status: OrderStatus