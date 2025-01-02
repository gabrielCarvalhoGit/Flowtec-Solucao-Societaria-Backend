from rest_framework.exceptions import NotFound

from apps.core.services.base_service import ServiceBase
from apps.societario.domain.entities.socio import SocioEntity

from apps.societario.infra.repositories.socio_repository import SocioRepository
from apps.societario.infra.repositories.formulario_abertura_repository import FormularioAberturaRepository


class SocioService(metaclass=ServiceBase):
    def __init__(
            self,
            repository=SocioRepository(),
            form_repository=FormularioAberturaRepository()
        ):

        self.__repository = repository
        self.__form_empresa_repository = form_repository
    
    def create_socios(self, **data):
        empresa_form_id = data.pop('empresa_id')
        socios = data.pop('socios')

        is_exists = self.__form_empresa_repository.exists_by_id(empresa_form_id)
        if not is_exists:
            raise NotFound('Formulário não encontrado.')

        response = [SocioEntity(empresa_id=empresa_form_id, **socio) for socio in socios]

        self.__repository.bulk_create(response)
        return response