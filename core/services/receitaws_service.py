import requests
from django.conf import settings
from rest_framework.exceptions import ValidationError


class ReceitaWsApiService:
    def __init__(self):
        self.api_key = settings.CNPJ_API_KEY
        self.api_url = settings.CNPJ_API_URL
    
    def get_data_cnpj(self, cnpj):
        url = f'{self.api_url}{cnpj}'
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()

            if data.get('status') == 'ERROR':
                raise ValidationError(f'Erro na API da ReceitaWS: {data.get('message')}')
            
            return data
        except requests.exceptions.Timeout:
            raise ValidationError('A requisição para a API da ReceitaWS expirou.')
        except requests.exceptions.RequestException as e:
            raise ValidationError(f'Erro ao consultar API da ReceitaWS: {str(e)}')