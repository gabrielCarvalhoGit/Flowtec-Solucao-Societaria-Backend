from rest_framework.exceptions import NotFound, ValidationError

from apps.core.services.base_service import ServiceBase
from apps.societario.repositories.etapa_processo_repository import EtapaProcessoRepository


class EtapaProcessoService(metaclass=ServiceBase):
    def __init__(self):
        self.repository = EtapaProcessoRepository()
    
    def get_etapa(self, etapa_id):
        if not etapa_id:
            raise ValidationError({'id': ['Parâmetro obrigatório.']})
        
        etapa = self.repository.get_etapa_by_id(etapa_id)

        if not etapa:
            raise NotFound('Etapa não encontrada.')
        
        return etapa
    
    def get_list_etapas(self):
        etapas = self.repository.get_etapas()

        if not etapas:
            raise NotFound('Nenhuma etapa cadastrada.')
        
        return etapas
