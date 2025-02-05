import uuid
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
    
    def filter_by_empresa(self, empresa_id: uuid.UUID) -> List[Socio]:
        return self.__model.objects.filter(empresa_id=empresa_id).select_related(
            'empresa',
            'endereco'
        )

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

    @transaction.atomic
    def bulk_update(self, list_obj: List[Socio], data: List[SocioEntity]):
        socios_to_update = []
        endereco_to_update = []

        for obj in list_obj:
            entity = next((s for s in data if s.id == obj.id))
            
            has_changes = False
            for field in obj._meta.fields:
                new_value = getattr(entity, field.name, None)
                
                if new_value:
                    if field.name != 'endereco' and getattr(obj, field.name) != new_value:
                        setattr(obj, field.name, new_value)
                        has_changes = True
                
            if has_changes:
                socios_to_update.append(obj)
            
            if not all(getattr(entity.endereco, data_field) == getattr(obj.endereco, data_field) for data_field in vars(entity.endereco)):
                endereco_to_update.append([obj.endereco, entity.endereco])
        
        if socios_to_update:
            update_fields = [field.name for field in self.__model._meta.fields if field.name not in ['id', 'endereco', 'empresa']]
            self.__model.objects.bulk_update(socios_to_update, update_fields)
        
        if endereco_to_update:
            self.__endereco_repository.bulk_update(*zip(*endereco_to_update))