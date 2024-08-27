import requests, os, dotenv

dotenv.load_dotenv()

API_KEY = os.getenv('API_KEY')

def validator_cpf(cpf):
    url = "https://api.invertexto.com/v1/validator"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {"value": cpf}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        return data 
    
    except requests.exceptions.RequestException as e:
        return {"error": str(e)} 

def formatar_resultado(data):
    if data.get("valid"):
        print("CPF válido")
        print(f"CPF formatado: {data.get('formatted')}")
    else:
        print("CPF inválido")


resultado = validator_cpf("04302304201")
formatar_resultado(resultado)
