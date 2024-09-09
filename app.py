import requests

def get_live_exchange_rate():
    url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json'
    
    # Sending a GET request to the API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Get the exchange rate for EGP under the USD object
        egp_rate = data.get('usd', {}).get('egp')
        
        if egp_rate:
            return egp_rate
        else:
            return "EGP exchange rate not found."
    else:
        return f"Failed to fetch data. Status code: {response.status_code}"
    
    



