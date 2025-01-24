import uuid
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

        if data.info_adicionais.resp_tecnica:
            self.__info_adicionais_repository.create(data.info_adicionais)

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
            info_adicionais_id=data.info_adicionais.id if data.info_adicionais.resp_tecnica else None,
            created_at=data.created_at
        )
    
    @transaction.atomic
    def update(self, obj: FormularioAberturaEmpresa, data: FormularioAberturaEmpresaEntity):
        if not all(getattr(data.endereco, field) == getattr(obj.endereco, field) for field in vars(data.endereco)):
            self.__endereco_repository.update(obj.endereco, data.endereco)
        
        if not obj.info_adicionais and data.info_adicionais:
            if data.info_adicionais.resp_tecnica:
                self.__info_adicionais_repository.create(data.info_adicionais)
                obj.info_adicionais_id = data.info_adicionais.id
        elif obj.info_adicionais and not data.info_adicionais.resp_tecnica:
            self.__info_adicionais_repository.delete(obj.info_adicionais)
            obj.info_adicionais_id = None
        elif data.info_adicionais and not all(getattr(data.info_adicionais, field) == getattr(obj.info_adicionais, field) for field in vars(data.info_adicionais)):
            self.__info_adicionais_repository.update(obj.info_adicionais, data.info_adicionais)

        for field in obj._meta.fields:
            if field.name not in ['endereco', 'processo', 'info_adicionais']:
                setattr(obj, field.name, getattr(data, field.name))
            
            obj.save()

    def get_by_id(self, form_id: uuid.UUID) -> FormularioAberturaEmpresa:
        try:
            return self.__model.objects.select_related(
                'processo',
                'endereco',
                'info_adicionais'
            ).prefetch_related(
                'socios'
            ).get(id=form_id)
        except self.__model.DoesNotExist:
            return None

    def exists_by_id(self, form_id: uuid.UUID) -> bool:
        return self.__model.objects.filter(id=form_id).exists()