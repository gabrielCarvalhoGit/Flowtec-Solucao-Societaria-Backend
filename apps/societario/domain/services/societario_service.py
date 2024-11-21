from django.db import transaction
from rest_framework.exceptions import ValidationError, NotFound

from apps.societario.domain.entities.abertura_empresa_entity import AberturaEmpresaEntity
from apps.societario.infra.repositories.societario_repository import (
    AberturaEmpresaRepository, 
    EnderecoRepository, 
    InfoAdicRepository
)

from apps.core.services.base_service import ServiceBase
from apps.contabilidades.services.contabilidade_service import ContService


class AberturaEmpresaService(metaclass=ServiceBase):
    def __init__(
            self, 
            societario_repository=AberturaEmpresaRepository(),
            endereco_repository=EnderecoRepository(),
            info_adic_repository=InfoAdicRepository(),
            cont_service=ContService()
        ):

        self.__repository = societario_repository
        self.__endereco_repository = endereco_repository
        self.__info_adic_repository=info_adic_repository
        self.__contabilidade_service = cont_service
    
    def get_empresa(self, id) -> AberturaEmpresaEntity:
        if not id:
            raise ValidationError({'id': ['Parâmetro obrigatório.']})
        
        empresa = self.__repository.get_by_id(id)
        if not empresa:
            raise NotFound('Empresa não encontrada')
        
        return AberturaEmpresaEntity.from_model(empresa)
    
    def create_empresa(self, request, **validated_data) -> AberturaEmpresaEntity:
        nome = validated_data.get('nome')
        contabilidade_id = validated_data.get('contabilidade_id', None)

        contabilidade = self.__contabilidade_service.get_contabilidade(contabilidade_id, request)
        response = AberturaEmpresaEntity.new(nome=nome, contabilidade=contabilidade)
        empresa = self.__repository.create(response)

        response.id = empresa.id
        response.created_at = empresa.created_at

        return response
    
    @transaction.atomic
    def formulario_abertura(self, **validated_data) -> AberturaEmpresaEntity:
        instance_id = validated_data.get('id')
        instance = self.__repository.get_by_id(instance_id)

        if not instance:
            raise NotFound('Processo não encontrado.')
        
        form_data = AberturaEmpresaEntity.validate_form(instance, **validated_data)

        endereco = self.__endereco_repository.create(form_data.pop('endereco'))
        info_adic = self.__info_adic_repository.create(form_data.pop('info_adic'))

        instance.endereco = endereco
        instance.info_adic = info_adic

        empresa = self.__repository.update(instance, **form_data)
        return AberturaEmpresaEntity.from_model(empresa)