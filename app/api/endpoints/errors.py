from app.api.models.error import Error

# Error definitions
error_404 = Error(code=404, message="Order not found")
error_400 = Error(code=400, message="Invalid Input")