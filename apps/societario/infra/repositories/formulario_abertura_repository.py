from django.db import transaction

from apps.societario.infra.models import FormularioAberturaEmpresa
from apps.societario.domain.entities.formulario_abertura import FormularioAberturaEmpresaEntity

from apps.societario.infra.repositories.endereco_repository import EnderecoRepository
from apps.societario.infra.repositories.info_adicionais_repository import InfoAdicionaisRepository


class FormularioAberturaRepository:
    def __init__(
            self, 
            model=FormularioAberturaEmpresa,
            endereco_repository=EnderecoRepository(),
            info_adic_repository=InfoAdicionaisRepository() 
        ):

        self.__model = model
        self.__endereco_repository = endereco_repository
        self.__info_adicionais_repository = info_adic_repository
    
    @transaction.atomic
    def create(self, data: FormularioAberturaEmpresaEntity):
        self.__endereco_repository.create(data.endereco)

        if data.info_adic.resp_tecnica:
            self.__info_adicionais_repository.create(data.info_adic)

        self.__model.objects.create(
            id=data.id,
            processo_id=data.processo.id,
            opcoes_nome_empresa=data.opcoes_nome_empresa,
            nome_fantasia=data.nome_fantasia,
            endereco_id=data.endereco.id,
            inscricao_imob=data.inscricao_imob,
            telefone=data.telefone,
            email=data.email,
            val_capital_social=data.val_capital_social,
            capital_integralizado=data.capital_integralizado,
            data_integralizacao=data.data_integralizacao,
            empresa_anexa_resid=data.empresa_anexa_resid,
            endereco_apenas_contato=data.endereco_apenas_contato,
            area_empresa=data.area_empresa,
            info_adic_id=data.info_adic.id,
            created_at=data.created_at
        )