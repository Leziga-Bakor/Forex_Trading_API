from pydantic import BaseModel, field_validator
from app.api.models.enums import OrderStatus

class OrderInput(BaseModel):
    """
    Represents an order input with stock information and quantity.

    Attributes:
        stoks (str): The stock symbol or identifier.
        quantity (float): The quantity of the stock to be ordered.
    """
    stoks: str
    quantity: float

    @field_validator("stoks")
    def validate_stoks(cls, v):
        """
        Validate the 'stoks' attribute to ensure it's not empty or containing only whitespace.

        Args:
            v (str): The 'stoks' attribute value to be validated.

        Raises:
            ValueError: If 'stoks' is empty or contains only whitespace.

        Returns:
            str: The validated 'stoks' attribute value.
        """
        if not v.strip():  # Check if the input is empty or contains only whitespace
            raise ValueError("stoks must not be empty or contain only whitespace")
        return v

    @field_validator("quantity")
    def validate_quantity(cls, v):
        """
        Validate the 'quantity' attribute to ensure it's a positive value.

        Args:
            v (float): The 'quantity' attribute value to be validated.

        Raises:
            ValueError: If 'quantity' is not a positive value.

        Returns:
            float: The validated 'quantity' attribute value.
        """
        if v <= 0: # check if the input is negative
            raise ValueError("quantity must be a positive value")
        return v

class OrderOutput(BaseModel):
    """
    Represents the output of an order operation with detailed information.

    Attributes:
        id (str): The unique identifier of the order.
        stoks (str): The stock symbol or identifier.
        quantity (float): The quantity of the stock ordered.
        status (OrderStatus): The status of the order, typically one of OrderStatus enum values.
    """
    id: str 
    stoks: str
    quantity: float
    status: OrderStatus