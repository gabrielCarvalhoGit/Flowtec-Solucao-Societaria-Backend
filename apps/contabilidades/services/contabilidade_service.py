from datetime import datetime
from rest_framework.exceptions import ValidationError, NotFound

from apps.contabilidades.models import Contabilidade
from apps.core.services.receitaws_service import ReceitaWsApiService
from apps.contabilidades.repositories.contabilidade_repository import ContRepository


class ContService:
    def __init__(self):
        self.repository = ContRepository()
        self.api_service = ReceitaWsApiService()
    
    def get_contabilidade(self, contabilidade_id=None, request=None):
        if not contabilidade_id:
            if request.user.contabilidade:
                return request.user.contabilidade
            else:
                raise NotFound('Nenhuma contabilidadade encontrada. Verifique se o usuário está vinculado a uma contabilidade ou informe o id da contabilidade que deseja consultar.')
        
        try:
            contabilidade = self.repository.get_by_id(contabilidade_id)
            return contabilidade
        except Contabilidade.DoesNotExist:
            raise NotFound('Contabilidade não encontrada.')

    def get_list_contabilidades(self):
        empresas = self.repository.get_contabilidades()

        if not empresas:
            raise NotFound('Nenhuma contabilidade cadastrada.')
        
        return empresas

    def create_cont(self, **validated_data):
        cnpj = self.api_service.validate_cnpj(validated_data['cnpj'])

        if self.repository.is_cont_exists(cnpj):
            raise ValidationError('O CNPJ informado já possui uma contabilidade cadastrada.')
        
        cont_data = self.api_service.get_data_cnpj(cnpj)

        validated_data['cnpj'] = cnpj
        validated_data['data_abertura'] = datetime.strptime(cont_data.get('abertura', ''), '%d/%m/%Y').strftime('%Y-%m-%d')
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
    
    def delete_cont(self, contabilidade_id):
        cont = self.get_contabilidade(contabilidade_id)
        self.repository.delete(cont)