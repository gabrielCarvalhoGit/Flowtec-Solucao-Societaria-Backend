from itertools import chain
from apps.societario.infra.models import Etapa, TipoProcesso, Tarefa


def create_etapas():
    etapa_data = [
        {"nome": "Proposta/formulário", "ordem": 1},
        {"nome": "Viabilidade", "ordem": 2},
        {"nome": "Registro", "ordem": 3},
        {"nome": "Alvarás", "ordem": 4},
        {"nome": "Tributação/NF", "ordem": 5},
        {"nome": "Concluído", "ordem": 6},
    ]

    objects = [Etapa(**data) for data in etapa_data]
    Etapa.objects.bulk_create(objects)

    return objects

def initialize_data():
    tarefas_data = []
    etapas = create_etapas()

    for etapa in etapas:
        if etapa.ordem == 1:
            tarefas_data.append([
                {"descricao": "Proposta enviada", "ordem": 1, "obrigatoria": True, "etapa_id": etapa.id},
                {"descricao": "Proposta aceita/formulário enviado", "ordem": 2, "obrigatoria": True, "etapa_id": etapa.id},
                {"descricao": "Formulário recebido/processo iniciado", "ordem": 3, "obrigatoria": True, "etapa_id": etapa.id}
            ])
        elif etapa.ordem == 2:
            tarefas_data.append([
                {"descricao": "Viabilidade solicitada", "ordem": 1, "obrigatoria": True, "etapa_id": etapa.id},
                {"descricao": "Viabilidade deferida", "ordem": 2, "obrigatoria": True, "etapa_id": etapa.id}
            ])
        elif etapa.ordem == 3:
            tarefas_data.append([
                {"descricao": "Documentos enviados para o cliente validar", "ordem": 1, "obrigatoria": True, "etapa_id": etapa.id},
                {"descricao": "E-CPF'S solicitados", "ordem": 2, "obrigatoria": True, "etapa_id": etapa.id},
                {"descricao": "Protocolado JUCESC", "ordem": 3, "obrigatoria": True, "etapa_id": etapa.id},
                {"descricao": "Liberado JUCESC", "ordem": 4, "obrigatoria": True, "etapa_id": etapa.id}
            ])
        elif etapa.ordem == 4:
            tarefas_data.append([
                {"descricao": "Bombeiros", "ordem": 1, "obrigatoria": False, "etapa_id": etapa.id},
                {"descricao": "Vigilância", "ordem": 2, "obrigatoria": False, "etapa_id": etapa.id},
                {"descricao": "Meio ambiente", "ordem": 3, "obrigatoria": False, "etapa_id": etapa.id},
                {"descricao": "Polícia", "ordem": 4, "obrigatoria": False, "etapa_id": etapa.id},
                {"descricao": "Inscrição estadual", "ordem": 5, "obrigatoria": False, "etapa_id": etapa.id},
                {"descricao": "Municipal", "ordem": 6, "obrigatoria": False, "etapa_id": etapa.id},
                {"descricao": "Conselho", "ordem": 7, "obrigatoria": False, "etapa_id": etapa.id}
            ])
        elif etapa.ordem == 5:
            tarefas_data.append([
                {"descricao": "Simples solicitado", "ordem": 1, "obrigatoria": True, "etapa_id": etapa.id},
                {"descricao": "Liberação de notas iniciada", "ordem": 2, "obrigatoria": True, "etapa_id": etapa.id},
                {"descricao": "Resultado simples liberado", "ordem": 3, "obrigatoria": True, "etapa_id": etapa.id},
                {"descricao": "NF liberada e configurada", "ordem": 4, "obrigatoria": True, "etapa_id": etapa.id}
            ])
        elif etapa.ordem == 6:
            tarefas_data.append([
                {"descricao": "Concluído", "ordem": 1, "obrigatoria": True, "etapa_id": etapa.id}
            ])
    
    tarefas_data = list(chain.from_iterable(tarefas_data))
    objects = [Tarefa(**data) for data in tarefas_data]
    
    Tarefa.objects.bulk_create(objects)

    tipos_processo_data = [
        {"descricao": "Abertura de empresa"},
        {"descricao": "Alteração contratual com regin"},
        {"descricao": "Alteração contratual sem regin/baixa"},
    ]

    objects = [TipoProcesso(**data) for data in tipos_processo_data]
    TipoProcesso.objects.bulk_create(objects)