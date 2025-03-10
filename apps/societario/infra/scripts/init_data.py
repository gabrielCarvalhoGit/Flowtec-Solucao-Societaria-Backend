from apps.societario.infra.models import Etapa, TipoProcesso


def initialize_data():
    etapas_data = [
        {"nome": "Proposta/formulário", "ordem": 1},
        {"nome": "Viabilidade", "ordem": 2},
        {"nome": "Registro", "ordem": 3},
        {"nome": "Alvarás", "ordem": 4},
        {"nome": "Simples/NF", "ordem": 5},
        {"nome": "Concluído", "ordem": 6},
    ]

    tipos_processo_data = [
        {"descricao": "Abertura de empresa"},
        {"descricao": "Alteração contratual com regin"},
        {"descricao": "Alteração contratual sem regin/baixa"},
    ]

    objects = [Etapa(**data) for data in etapas_data]
    Etapa.objects.bulk_create(objects)

    objects = [TipoProcesso(**data) for data in tipos_processo_data]
    TipoProcesso.objects.bulk_create(objects)