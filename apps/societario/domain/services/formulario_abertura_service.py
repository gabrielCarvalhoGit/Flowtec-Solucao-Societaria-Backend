from rest_framework.exceptions import ValidationError

from apps.core.services.base_service import ServiceBase
from apps.societario.domain.services.processo_service import ProcessoService

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

        response = FormularioAberturaEmpresaEntity(**data)

        self.__repository.create(response)
        return response