from typing import List
from django.db import transaction

from apps.societario.infra.models import Socio
from apps.societario.domain.entities.socio import SocioEntity

from apps.societario.infra.repositories.endereco_repository import EnderecoRepository


class SocioRepository:
    def __init__(
            self, 
            model=Socio,
            endereco_repository=EnderecoRepository()
        ):

        self.__model = model
        self.__endereco_repository = endereco_repository
    
    @transaction.atomic
    def bulk_create(self, data: List[SocioEntity]):
        model_instances = []
        endereco_entities = []

        for item in data:
            socio = self.__model(
                id=item.id,
                empresa_id=item.empresa_id,
                nome=item.nome,
                nacionalidade=item.nacionalidade,
                data_nascimento=item.data_nascimento,
                estado_civil=item.estado_civil,
                regime_casamento=item.regime_casamento,
                profissao=item.profissao,
                cpf=item.cpf,
                rg=item.rg,
                orgao_expedidor=item.orgao_expedidor,
                uf=item.uf,
                administrador=item.administrador,
                tipo_administrador=item.tipo_administrador,
                qtd_cotas=item.qtd_cotas,
                endereco_id=item.endereco.id,
                created_at=item.created_at
            )
            endereco = item.endereco

            model_instances.append(socio)
            endereco_entities.append(endereco)

        self.__endereco_repository.bulk_create(endereco_entities)
        self.__model.objects.bulk_create(model_instances)