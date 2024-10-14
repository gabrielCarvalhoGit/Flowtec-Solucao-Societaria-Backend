from datetime import datetime
from rest_framework.exceptions import ValidationError, NotFound

from apps.core.services.receitaws_service import ReceitaWsApiService

from apps.empresas.models import Empresa
from apps.empresas.repositories.empresa_repository import EmpresaRepository

from apps.contabilidades.services.contabilidade_service import ContService


class EmpresaService:
    def __init__(self):
        self.repository = EmpresaRepository()

        self.api_service = ReceitaWsApiService()
        self.cont_service = ContService()

    def get_empresa(self, empresa_id):
        try:
            empresa = self.repository.get_by_id(empresa_id)
            return empresa
        except Empresa.DoesNotExist:
            raise NotFound('Empresa não encontrada.')

    def create_empresa(self, **validated_data):
        cnpj = self.api_service.validate_cnpj(validated_data['cnpj'])
        contabilidade = self.cont_service.get_contabilidade(validated_data['contabilidade_id'])

        if self.repository.is_empresa_exists(cnpj):
            raise ValidationError('O CNPJ informado já possui uma empresa cadastrada.')
        
        empresa_data = self.api_service.get_data_cnpj(cnpj)

        validated_data['cnpj'] = cnpj
        validated_data['data_abertura'] = datetime.strptime(empresa_data.get('abertura', ''), '%d/%m/%Y').strftime('%Y-%m-%d')
        validated_data['situacao'] = empresa_data.get('situacao', '')
        validated_data['tipo'] = empresa_data.get('tipo', '')
        validated_data['nome'] = empresa_data.get('nome', '')
        validated_data['nome_fantasia'] = empresa_data.get('fantasia', '')
        validated_data['porte'] = empresa_data.get('porte', '')
        validated_data['natureza_juridica'] = empresa_data.get('natureza_juridica', '')

        atividade_principal = empresa_data.get('atividade_principal', [{}])[0]
        validated_data['cod_atividade_principal'] = atividade_principal.get('code', '')
        validated_data['desc_atividade_principal'] = atividade_principal.get('text', '')

        endereco = f"{empresa_data.get('logradouro', '')}, {empresa_data.get('numero', '')}, {empresa_data.get('bairro', '')}, {empresa_data.get('municipio', '')} - {empresa_data.get('uf', '')}"
        validated_data['endereco'] = endereco
        validated_data['cep'] = empresa_data.get('cep', '')

        validated_data['contabilidade'] = contabilidade

        empresa = self.repository.create(**validated_data)
        return empresa
        
    def delete_empresa(self, empresa_id):
        empresa = self.get_empresa(empresa_id)
        self.repository.delete(empresa)