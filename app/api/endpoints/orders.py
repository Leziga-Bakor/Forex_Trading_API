import random
import time
from fastapi import APIRouter, HTTPException
from app.api.models.order import OrderInput, OrderOutput
from app.api.models.enums import OrderStatus
from app.api.endpoints.errors import error_404


router = APIRouter()

orders_db = {}
order_count=0

def random_delay():
    """
    Introduces a random delay between 0.1 and 1 second by sleeping for a random duration.

    Example usage:
        random_delay()  # Introduces a random delay between 0.1 and 1 second.
    """
    random_delay = random.uniform(0.1, 1)
    time.sleep(random_delay)


@router.get("/")
async def read_root():
    """
    Retrieve a simple message indicating the Forex Trading Platform API's root endpoint.

    Returns:
        dict: A dictionary containing a message indicating the API's root endpoint.
    """
    return {"message": "Welcome to Forex Trading Platform API"}


@router.get("/orders")
async def get_orders(): 
    """
    Retrieve a list of orders from the Forex Trading Platform API.

    Returns:
        List[dict]: A list of dictionaries, each representing an order.

    """
    random_delay()
    orders = list(orders_db.values())
    return orders


@router.post("/orders",status_code=201)
async def create_order(order: OrderInput):
    """
    Create a new order and add it to the Forex Trading Platform API.

    Args:
        order (OrderInput): The order input containing stock information and quantity.

    Returns:
        OrderOutput: The newly created order with a unique ID and a pending status.

    """
    random_delay()
    global order_count 
    order_count += 1
    new_order = OrderOutput(id=str(order_count), stoks=order.stoks, quantity=order.quantity, status=OrderStatus.pending)
    orders_db[int(new_order.id)] = new_order
    return new_order

@router.get("/orders/{orderid}")
async def get_order_byID(orderid: int):
    """
    Retrieve an order by its unique ID.

    Args:
        orderid (int): The unique identifier of the order to retrieve.

    Returns:
        OrderOutput: The order with the specified ID.

    Raises:
        HTTPException: If the order with the given ID is not found, an HTTP 404 error is raised.
    """
    random_delay()
    if orderid not in orders_db:
        raise HTTPException(status_code=404, detail=error_404.model_dump())
    return orders_db[orderid]

@router.delete("/orders/{orderid}", status_code=204)
async def cancelOrder(orderid: int):
    """
    Cancel an order by its unique ID.

    Args:
        orderid (int): The unique identifier of the order to cancel.

    Returns:
        None

    Raises:
        HTTPException: If the order with the given ID is not found, an HTTP 404 error is raised.
    """
    random_delay()
    if orderid not in orders_db:
        raise HTTPException(status_code=404, detail=error_404.model_dump())
    cancelled_order = orders_db[orderid]
    cancelled_order.status=OrderStatus.canceled
    return 