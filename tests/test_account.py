import pytest
import requests

BASE_URL = "https://parabank.parasoft.com/parabank/services/bank"

def test_get_account_balance():
    account_id = 12345
    response = requests.get(f"{BASE_URL}/accounts/{account_id}")
    assert response.status_code == 200
    
    assert "<account>" in response.text
    assert "<balance>" in response.text

@pytest.mark.skip(reason="Transfer endpoint demo API'de çalışmıyor veya 404 dönüyor")
def test_transfer_funds():
    transfer_data = {
        "fromAccountId": 12345,
        "toAccountId": 54321,
        "amount": 100.0
    }
    response = requests.post(f"{BASE_URL}/transfers", json=transfer_data)
    assert response.status_code in [200, 201]
