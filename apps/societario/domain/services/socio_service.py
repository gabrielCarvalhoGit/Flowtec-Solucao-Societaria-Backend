from rest_framework.exceptions import NotFound, ValidationError

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
    
    def update_socios(self, **data):
        empresa_form_id = data.pop('empresa_id')
        socios = data.pop('socios')

        is_exists = self.__form_empresa_repository.exists_by_id(empresa_form_id)
        if not is_exists:
            raise NotFound('Formulário não encontrado.')
        
        socios_empresa = self.__repository.filter_by_empresa(empresa_form_id)
        if socios_empresa.exists() == 0:
            raise ValidationError('A empresa informada não possui nenhum sócio para atualizar.')
        
        response = [SocioEntity.from_model(socio_empresa) for socio_empresa in socios_empresa]

        for socio in socios:
            socio_entity = next((s for s in response if s.id == socio['id']), None)

            if not socio_entity:
                raise ValidationError(f'Sócio {socio['id']} não encontrado para a empresa informada.')
            
            socio_entity.update(**socio)
        
        self.__repository.bulk_update(socios_empresa, response)
        return response