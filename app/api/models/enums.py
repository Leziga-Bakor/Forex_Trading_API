from enum import Enum

class OrderStatus(str, Enum):
    pending = "pending"
    executed = "executed"
    canceled = "canceled"
