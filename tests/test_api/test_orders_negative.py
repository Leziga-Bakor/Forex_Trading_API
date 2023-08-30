import pytest
import requests

def test_get_nonexistent_order(base_url):
    response = requests.get(f"{base_url}/orders/999")
    assert response.status_code == 404
    

def test_cancel_nonexistent_order(base_url):
    response = requests.delete(f"{base_url}/orders/999")
    assert response.status_code == 404
    
