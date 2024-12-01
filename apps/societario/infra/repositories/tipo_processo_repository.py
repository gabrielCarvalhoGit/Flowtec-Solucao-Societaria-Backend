import uuid
from typing import Optional, List

from apps.societario.infra.models import TipoProcesso


class TipoProcessoRepository:
    def __init__(self, model=TipoProcesso):
        self.__model = model

    def get_by_id(self, id: uuid.UUID) -> Optional[TipoProcesso]:
        try:
            return self.__model.objects.get(id=id)
        except self.__model.DoesNotExist:
            return None
    
    def list_tipo_processo(self) -> List[TipoProcesso]:
        return self.__model.objects.all()