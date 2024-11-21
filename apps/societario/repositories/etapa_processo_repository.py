from apps.societario.infra.models.etapa_model import Etapa

class EtapaProcessoRepository:
    def get_etapa_by_id(self, etapa_id):
        try:
            return Etapa.objects.get(id=etapa_id)
        except Etapa.DoesNotExist:
            return None
    
    def get_etapas(self):
        return Etapa.objects.all()