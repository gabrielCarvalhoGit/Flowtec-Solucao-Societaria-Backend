import uuid
from typing import List
from rest_framework.exceptions import ValidationError, NotFound

from apps.core.services.base_service import ServiceBase
from apps.societario.domain.entities.etapa import EtapaEntity
from apps.societario.infra.repositories.etapa_repository import EtapaRepository


class EtapaService(metaclass=ServiceBase):
    def __init__(
            self,
            etapa_repository = EtapaRepository()
        ):
        
        self.__repository = etapa_repository
    
    def get_etapa(self, id: uuid.UUID) -> EtapaEntity:
        if not id:
            raise ValidationError({'etapa_id': ['Parâmetro obrigatório.']})
        
        etapa = self.__repository.get_by_id(id)
        if not etapa:
            raise NotFound('Etapa não encontrada.')
        
        return EtapaEntity.from_model(etapa)
    
    def list_etapas(self) -> List[EtapaEntity]:
        etapas = self.__repository.list_etapas()
        return [EtapaEntity.from_model(etapa) for etapa in etapas]