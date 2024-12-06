import uuid
from typing import Optional, List

from apps.societario.infra.models import Etapa


class EtapaRepository:
    def __init__(self, model=Etapa):
        self.__model = model
    
    def get_by_id(self, etapa_id: uuid.UUID) -> Optional[Etapa]:
        try:
            return self.__model.objects.get(id=etapa_id)
        except self.__model.DoesNotExist:
            return None
    
    def list_etapas(self) -> List[Etapa]:
        return self.__model.objects.all().order_by('ordem')
    
    def list_processos_by_etapa(self):
        return self.__model.objects.prefetch_related('processos')