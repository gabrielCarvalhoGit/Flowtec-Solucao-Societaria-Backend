import uuid
from rest_framework.exceptions import NotFound

from apps.core.services.base_service import ServiceBase
from apps.societario.domain.services.processo_service import ProcessoService

from apps.societario.domain.entities.endereco import EnderecoEntity
from apps.societario.domain.entities.info_adicionais import InfoAdicionaisEntity
from apps.societario.domain.entities.formulario_abertura import FormularioAberturaEmpresaEntity
from apps.societario.infra.repositories.formulario_abertura_repository import FormularioAberturaRepository


class FormularioAberturaService(metaclass=ServiceBase):
    def __init__(
            self,
            repository=FormularioAberturaRepository(),
            processo_service=ProcessoService()
        ):

        self.__repository = repository
        self.__processo_service = processo_service
    
    def create_form(self, **data) -> FormularioAberturaEmpresaEntity:
        processo_id = data.pop('processo_id')

        processo = self.__processo_service.get_processo(processo_id)
        data['processo'] = processo

        endereco = EnderecoEntity(**data['endereco'])
        data['endereco'] = endereco

        info_adicionais = InfoAdicionaisEntity(**data['info_adicionais'])
        data['info_adicionais'] = info_adicionais

        response = FormularioAberturaEmpresaEntity(**data)

        self.__repository.create(response)
        return response
    
    def exists_form(self, id: uuid.UUID):
        if not self.__repository.exists_by_id(id):
            raise NotFound('Formulário não encontrado.')