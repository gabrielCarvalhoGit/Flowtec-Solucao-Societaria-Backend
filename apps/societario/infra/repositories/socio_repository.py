from typing import List
from dataclasses import asdict
from apps.societario.infra.models import Socio
from apps.societario.domain.entities.socio import SocioEntity


class SocioRepository:
    def __init__(self, model=Socio):
        self.__model = model
    
    def bulk_create(self, data: List[SocioEntity]):
        model_instances = [
            Socio(
                id=item.id,
                empresa_id=item.empresa.id,
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
            ) for item in data
        ]

        self.__model.objects.bulk_create(model_instances)