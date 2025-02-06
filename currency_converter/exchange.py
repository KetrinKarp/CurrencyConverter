import requests

API_URL = "https://api.exchangerate-api.com/v4/latest"

def get_exchange_rate(base_currency: str, target_currency: str) -> float:
    response = requests.get(f"{API_URL}/{base_currency}")
    data = response.json()
    
    if response.status_code != 200 or "rates" not in data:
        raise ValueError("Invalid response from exchange rate API")
    
    rates = data['rates']
    if target_currency not in rates:
        raise ValueError(f"Target currency {target_currency} is not supported")
    
    return rates[target_currency]

def convert_amount(base_currency: str, target_currency: str, amount: float) -> float:
    rate = get_exchange_rate(base_currency, target_currency)
    return amount * rate

def get_supported_currencies() -> list:
    response = requests.get(f"{API_URL}/USD")
    data = response.json()
    
    if response.status_code != 200 or "rates" not in data:
        raise ValueError("Unable to fetch supported currencies")
    
    return list(data['rates'].keys())
