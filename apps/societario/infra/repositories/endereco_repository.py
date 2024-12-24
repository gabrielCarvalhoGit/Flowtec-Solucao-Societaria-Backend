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