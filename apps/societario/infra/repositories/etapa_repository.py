import uuid
from typing import Optional, List

from django.db import transaction
from django.db.models import Prefetch

from apps.societario.infra.models import Etapa, Processo


class EtapaRepository:
    def __init__(self, model=Etapa):
        self.__model = model
    
    def get_by_id(self, etapa_id: uuid.UUID) -> Optional[Etapa]:
        try:
            return self.__model.objects.get(id=etapa_id)
        except self.__model.DoesNotExist:
            return None
    
    def get_by_ordem(self, ordem):
        return self.__model.objects.get(ordem=ordem)
    
    def list_etapas(self) -> List[Etapa]:
        return self.__model.objects.all().order_by('ordem')
    
    @transaction.atomic
    def list_processos_by_etapa(self):
        return self.__model.objects.prefetch_related(
            Prefetch('processos', queryset=Processo.objects.order_by('expire_at'))
        ).order_by('ordem')