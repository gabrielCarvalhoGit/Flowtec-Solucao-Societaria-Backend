from apps.societario.models import AberturaEmpresa, Etapa, Processo, ProcessosEtapa


class SocietarioRepository:
    def create_registro_empresa(self, nome, contabilidade, etapa):
        empresa = AberturaEmpresa.objects.create(
            nome=nome, 
            contabilidade=contabilidade,
            etapa=etapa
        )
        return empresa
    
    def get_etapa(self, nome_etapa):
        try:
            return Etapa.objects.get(nome_etapa=nome_etapa)
        except Etapa.DoesNotExist:
            return None
    
    def create_processos_etapa_empresa(self, etapa, empresa):
        processos_etapa = ProcessosEtapa.objects.filter(etapa=etapa)

        for processo_etapa in processos_etapa:
            Processo.objects.create(
                etapa=etapa,
                empresa=empresa,
                nome_processo=processo_etapa.nome_processo,
                status_processo=False
            )