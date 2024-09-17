import requests


api_key = 'c4db9935f7dbb1dddfca8c73f60d92efa15228f8dd47443709fdaa2c76f9c93f'
cnpj = '00000000000000'

url = f'https://www.receitaws.com.br/v1/cnpj/{cnpj}'

headers = {
    'Authorization': f'Bearer {api_key}',
}

response = requests.get(url, headers=headers)
data = response.json()
print(data, response.status_code)