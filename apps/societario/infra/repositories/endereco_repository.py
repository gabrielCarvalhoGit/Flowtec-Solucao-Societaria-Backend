from typing import List

from apps.societario.infra.models import Endereco
from apps.societario.domain.entities.endereco import EnderecoEntity


class EnderecoRepository:
    def __init__(self, model=Endereco):
        self.__model = model
    
    def create(self, data: EnderecoEntity):
        self.__model.objects.create(
            id=data.id,
            rua=data.rua,
            numero=data.numero,
            bairro=data.bairro,
            complemento=data.complemento,
            cep=data.cep,
            municipio=data.municipio,
            uf=data.uf
        )
    
    def update(self, obj: Endereco, data: EnderecoEntity):
        for field in obj._meta.fields:
            setattr(obj, field.name, getattr(data, field.name))
        
        obj.save()

    def bulk_create(self, data: List[EnderecoEntity]):
        model_instances = [
            self.__model(
                id=item.id,
                rua=item.rua,
                numero=item.numero,
                bairro=item.bairro,
                complemento=item.complemento,
                cep=item.cep,
                municipio=item.municipio,
                uf=item.uf
            ) for item in data
        ]

        self.__model.objects.bulk_create(model_instances)
    
    def bulk_update(self, list_obj: List[Endereco], data: List[EnderecoEntity]):
        endereco_to_update = []

        for obj in list_obj:
            entity = next((s for s in data if s.id == obj.id))

            has_changes = False
            for field in obj._meta.fields:
                new_value = getattr(entity, field.name, None)

                if new_value and getattr(obj, field.name) != new_value:
                    setattr(obj, field.name, new_value)
                    has_changes = True
                
            if has_changes:
                endereco_to_update.append(obj)
        
        if endereco_to_update:
            self.__model.objects.bulk_update(endereco_to_update, [field.name for field in self.__model._meta.fields if field.name != 'id'])