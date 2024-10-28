from rest_framework.exceptions import NotFound, ValidationError

from apps.contabilidades.services.contabilidade_service import ContService
from apps.societario.repositories.societario_repository import SocietarioRepository


class SocietarioService:
    def __init__(self):
        self.cont_service = ContService()
        self.repository = SocietarioRepository()

    def registrar_empresa(self, contabilidade_id, request):
        try:
            contabilidade = self.cont_service.get_contabilidade(contabilidade_id, request)
            
            nome_registro = request.data.get('nome')
            if not nome_registro:
                raise ValidationError({'nome': ["Este campo é obrigatório."]})
            
            etapa_inicial = self.repository.get_etapa('Proposta/formulário')
            if not etapa_inicial:
                raise NotFound("Etapa 'Proposta/formulário' não encontrada.")
            
            empresa = self.repository.create_registro_empresa(nome_registro, contabilidade, etapa_inicial)
            self.repository.create_processos_etapa_empresa(etapa_inicial, empresa)

            return empresa
        except Exception as e:
            raise ValidationError(str(e))