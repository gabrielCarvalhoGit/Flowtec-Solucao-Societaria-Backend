import uuid
from typing import Optional
from apps.societario.infra.models import AberturaEmpresa, Endereco, InfoAdic

from apps.societario.domain.entities.endereco_entity import EnderecoEntity
from apps.societario.domain.entities.info_adic_entity import InfoAdicEntity
from apps.societario.domain.entities.abertura_empresa_entity import AberturaEmpresaEntity


class AberturaEmpresaRepository:
    def __init__(self, model=AberturaEmpresa):
        self.__model = model

    def get_by_id(self, id: uuid) -> Optional[AberturaEmpresa]:
        try:
            return self.__model.objects.get(id=id)
        except self.__model.DoesNotExist:
            return None

    def create(self, data: AberturaEmpresaEntity) -> AberturaEmpresa:
        return self.__model.objects.create(
            nome=data.nome,
            contabilidade=data.contabilidade,
            expire_at=data.expire_at
        )
    
    def update(self, instance: AberturaEmpresa, **validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        
        instance.save()
        return instance

class EnderecoRepository:
    def __init__(self, model=Endereco):
        self.__model = model
    
    def create(self, data: EnderecoEntity) -> Endereco:
        return self.__model.objects.create(
            endereco_completo=data.endereco_completo,
            complemento=data.complemento,
            cep=data.cep
        )

class InfoAdicRepository:
    def __init__(self, model=InfoAdic):
        self.__model = model
    
    def create(self, data: InfoAdicEntity):
        return self.__model.objects.create(
            resp_tecnica=data.resp_tecnica,
            nome_reponsavel=data.nome_reponsavel,
            nmr_carteira_profissional=data.nmr_carteira_profissional,
            uf=data.uf,
            area_resp=data.area_resp
        )