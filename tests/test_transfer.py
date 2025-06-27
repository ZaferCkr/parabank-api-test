import requests

BASE_URL = "https://parabank.parasoft.com/parabank/services/bank"

def test_transfer_success():
    transfer_data = {
        "fromAccountId": 12345,   # Var olan ve yeterli bakiyesi olan hesap
        "toAccountId": 54321,     # Var olan başka hesap
        "amount": 100.0
    }
    response = requests.post(f"{BASE_URL}/transfers", json=transfer_data)
    assert response.status_code in [200, 201]
    # İstersen response içeriğini de kontrol edebilirsin
    assert "transferId" in response.text or "success" in response.text.lower()

def test_transfer_insufficient_balance():
    transfer_data = {
        "fromAccountId": 12345,
        "toAccountId": 54321,
        "amount": 9999999.99  # Çok büyük tutar, bakiye yetersiz
    }
    response = requests.post(f"{BASE_URL}/transfers", json=transfer_data)
    assert response.status_code == 400  # Genelde 400 veya uygun hata kodu olur

def test_transfer_invalid_account():
    transfer_data = {
        "fromAccountId": 12345,
        "toAccountId": 99999,  # Olmayan hesap
        "amount": 100.0
    }
    response = requests.post(f"{BASE_URL}/transfers", json=transfer_data)
    assert response.status_code == 404  # Hesap bulunamazsa 404 beklenebilir
