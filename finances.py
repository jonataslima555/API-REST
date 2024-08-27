import requests

API_KEY = 'api_key'

def get_stock_quote(symbol):
    url = f'https://www.alphavantage.co/query'
    params = {
        'function': 'GLOBAL_QUOTE',
        'symbol': symbol,
        'apikey': API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if 'Global Quote' in data:
        return data['Global Quote']
    else:
        return {"error": "Dados não encontrados"}


symbol = 'AAPL' 
quote = get_stock_quote(symbol)

if 'error' not in quote:
    print(f"Cotação para {symbol}:")
    print(f"Preço atual: ${quote['05. price']}")
    print(f"Data da última negociação: {quote['07. latest trading day']}")
else:
    print(quote['error'])
