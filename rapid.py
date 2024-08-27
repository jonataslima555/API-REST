import requests, dotenv, os

# Carregar as variáveis de ambiente
dotenv.load_dotenv()

# Obtenha a chave da API do RapidAPI do arquivo .env
API_KEY = os.getenv("API_KEY3")

# Verifica se a chave foi carregada corretamente
if not API_KEY:
    raise ValueError("API_KEY3 não encontrada no arquivo .env")

# Defina a URL da API e os cabeçalhos
symbol = "AAPL"  # Símbolo da Apple na bolsa
url = "https://yahoo-finance15.p.rapidapi.com/api/yahoo/finance/quote"

querystring = {"symbol": symbol}

headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "yahoo-finance15.p.rapidapi.com"
}

# Faça a solicitação GET à API
response = requests.get(url, headers=headers, params=querystring)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Parseia a resposta JSON
    # Extraia o preço atual da ação
    if 'quotes' in data and data['quotes']:
        current_price = data['quotes'][0].get("regularMarketPrice")
        print(f"O preço atual da ação da Apple (AAPL) é: ${current_price}")
    else:
        print("Dados não encontrados.")
else:
    print(f"Erro ao acessar a API: {response.status_code}")
    print(response.text)  # Exibe a mensagem de erro retornada pela API
