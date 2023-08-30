import random
import time
from fastapi import APIRouter, HTTPException
from app.api.models.order import OrderInput, OrderOutput
from app.api.models.enums import OrderStatus
from app.api.endpoints.errors import error_404

router = APIRouter()

orders_db = {}
order_count=0


@router.get("/")
def read_root():
    return {"message": "Forex Trading Platform API"}

@router.get("/orders")
def get_orders(): 
    orders = list(orders_db.values())
    return orders

@router.post("/orders",status_code=201)
def create_order(order: OrderInput):
    global order_count 
    order_count += 1
    new_order = OrderOutput(id=str(order_count), stoks=order.stoks, quantity=order.quantity, status=OrderStatus.pending)
    orders_db[int(new_order.id)] = new_order
    return new_order

@router.get("/orders/{orderid}")
def get_order_byID(orderid: int):
    if orderid not in orders_db:
        raise HTTPException(status_code=404, detail=error_404.model_dump())
    return orders_db[orderid]

@router.delete("/orders/{orderid}",status_code=204)
async def cancelOrder(orderid: int):
    """Cancel and Order"""
    if orderid not in orders_db:
        raise HTTPException(status_code=404, detail=error_404.model_dump())
    deleted_order = orders_db.pop(orderid)
    return deleted_order