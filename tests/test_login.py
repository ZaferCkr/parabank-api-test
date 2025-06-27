import requests

BASE_URL = "https://parabank.parasoft.com/parabank/services/bank"

def test_get_existing_customer():
    response = requests.get(f"{BASE_URL}/customers/12212")
    assert response.status_code == 200
    assert "John" in response.text

def test_get_non_existing_customer():
    response = requests.get(f"{BASE_URL}/customers/99999")
    assert response.status_code in [400, 404]

