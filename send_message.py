import requests


BASE_URL = 'http://localhost:8080'
INSTANCE_NAME = 'instance_name'  # Substitua pelo nome da sua instância
EVOLUTION_AUTHENTICATION_API_KEY = 'key_code'  # Substitua pela sua chave de API

headers = {
    'apikey': EVOLUTION_AUTHENTICATION_API_KEY,
    'Content-Type': 'application/json'
}
payload = {
    'number': 'phone_number',  # Substitua por um número de telefone válido
    'text': 'Olá PycodeBR!',
    # 'delay': 10000, # simular "digitando"
}
response = requests.post(
    url=f'{BASE_URL}/message/sendText/{INSTANCE_NAME}',
    json=payload,
    headers=headers,
)
print(response.json())
