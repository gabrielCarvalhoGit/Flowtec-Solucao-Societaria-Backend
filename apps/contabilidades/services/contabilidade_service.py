import re
from datetime import datetime
from rest_framework.exceptions import ValidationError

from core.services.receitaws_service import ReceitaWsApiService
from apps.contabilidades.repositories.contabilidade_repository import ContRepository


class ContService:
    def __init__(self):
        self.repository = ContRepository()
        self.api_service = ReceitaWsApiService()
    
    def create_cont(self, **validated_data):
        cnpj = self.validate_cnpj(validated_data['cnpj'])
        cont_data = self.api_service.get_data_cnpj(cnpj)

        validated_data['cnpj'] = cnpj
        validated_data['abertura'] = datetime.strptime(cont_data.get('abertura', ''), '%d/%m/%Y').strftime('%Y-%m-%d')
        validated_data['situacao'] = cont_data.get('situacao', '')
        validated_data['tipo'] = cont_data.get('tipo', '')
        validated_data['nome'] = cont_data.get('nome', '')
        validated_data['nome_fantasia'] = cont_data.get('fantasia', '')
        validated_data['porte'] = cont_data.get('porte', '')
        validated_data['natureza_juridica'] = cont_data.get('natureza_juridica', '')

        atividade_principal = cont_data.get('atividade_principal', [{}])[0]
        validated_data['cod_atividade_principal'] = atividade_principal.get('code', '')
        validated_data['desc_atividade_principal'] = atividade_principal.get('text', '')

        endereco = f"{cont_data.get('logradouro', '')}, {cont_data.get('numero', '')}, {cont_data.get('bairro', '')}, {cont_data.get('municipio', '')} - {cont_data.get('uf', '')}"
        validated_data['endereco'] = endereco
        validated_data['cep'] = cont_data.get('cep', '')

        contabilidade = self.repository.create(**validated_data)
        return contabilidade
    
    def validate_cnpj(self, cnpj):
        cnpj = re.sub(r'\D', '', cnpj)

        if len(cnpj) != 14:
            raise ValidationError('CNPJ deve ter 14 dígitos.')
        
        if self.repository.is_cont_exists(cnpj):
            raise ValidationError('O CNPJ informado já possui uma contabilidade cadastrada.')
        
        return cnpj