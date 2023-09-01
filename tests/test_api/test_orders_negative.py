import pytest
import requests

def test_get_nonexistent_order(base_url):
    response = requests.get(f"{base_url}/orders/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == {"code": 404, "message": "Order not found"}

def test_cancel_nonexistent_order(base_url):
    response = requests.delete(f"{base_url}/orders/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == {"code": 404, "message": "Order not found"}
    
def test_get_wrongendpoint(base_url):
    response = requests.get(f"{base_url}/sale")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

def test_delete_wrongendpoint(base_url):
    response = requests.delete(f"{base_url}/sale")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}

def test_post_wrontendpoint(base_url):
    order_data = {"stocks": "USDGBP", "quantity": 30}
    response = requests.post(f"{base_url}", json=order_data)
    assert response.status_code == 405