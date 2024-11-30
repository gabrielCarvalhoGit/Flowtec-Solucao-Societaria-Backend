import uuid
from rest_framework.exceptions import ValidationError, NotFound

from apps.core.services.base_service import ServiceBase
from apps.societario.domain.entities.etapas_entity import EtapasEntity
from apps.societario.infra.repositories.etapas_repository import EtapasRepository


class EtapasService(metaclass=ServiceBase):
    def __init__(
            self,
            etapa_repository = EtapasRepository()
        ):
        
        self.__repository = etapa_repository
    
    def get_etapa(self, id: uuid) -> EtapasEntity:
        if not id:
            raise ValidationError({'id': ['Parâmetro obrigatório.']})
        
        etapa = self.__repository.get_by_id(id)
        if not etapa:
            raise NotFound('Etapa não encontrada.')
        
        return EtapasEntity.from_model(etapa)