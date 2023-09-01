from enum import Enum

class OrderStatus(str, Enum):
    """
    Enum representing the status of an order.

    Attributes:
        pending (str): Indicates that the order is pending and has not been executed.
        executed (str): Indicates that the order has been executed or completed.
        canceled (str): Indicates that the order has been canceled.
    """
    pending = "pending"
    executed = "executed"
    canceled = "cancelled"
