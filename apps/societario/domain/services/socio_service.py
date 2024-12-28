from apps.core.services.base_service import ServiceBase
from apps.societario.domain.services.formulario_abertura_service import FormularioAberturaService

from apps.societario.domain.entities.socio import SocioEntity
from apps.societario.infra.repositories.socio_repository import SocioRepository


class SocioService(metaclass=ServiceBase):
    def __init__(
            self,
            repository=SocioRepository(),
            form_service=FormularioAberturaService()
        ):

        self.__repository = repository
        self.__form_empresa_service = form_service
    
    def create_socios(self, **data):
        empresa_form_id = data.pop('empresa_id')
        socios = data.pop('socios')

        self.__form_empresa_service.exists_form(empresa_form_id)

        response = [SocioEntity(empresa_id=empresa_form_id, **socio) for socio in socios]

        self.__repository.bulk_create(response)
        return response