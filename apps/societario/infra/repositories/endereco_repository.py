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