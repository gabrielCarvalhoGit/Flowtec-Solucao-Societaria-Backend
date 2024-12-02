import uuid
from typing import List
from rest_framework.exceptions import ValidationError, NotFound

from apps.core.services.base_service import ServiceBase
from apps.societario.domain.entities.tipo_processo_entity import TipoProcessoEntity
from apps.societario.infra.repositories.tipo_processo_repository import TipoProcessoRepository


class TipoProcessoService(metaclass=ServiceBase):
    def __init__(
            self,
            tipo_processo_repository = TipoProcessoRepository()
        ):

        self.__repository = tipo_processo_repository
    
    def get_tipo_processo(self, id: uuid.UUID) -> TipoProcessoEntity:
        if not id:
            raise ValidationError({'tipo_processo_id': 'Parâmetro obrigatório.'})
        
        tipo_processo = self.__repository.get_by_id(id)
        if not tipo_processo:
            raise NotFound('Tipo do processo não encontrado.')
        
        return TipoProcessoEntity.from_model(tipo_processo)
    
    def list_tipo_processo(self) -> List[TipoProcessoEntity]:
        tipos_processo = self.__repository.list_tipo_processo()
        return [TipoProcessoEntity.from_model(tipo_processo) for tipo_processo in tipos_processo]