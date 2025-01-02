import uuid
from rest_framework.exceptions import ValidationError, NotFound

from apps.core.services.base_service import ServiceBase
from apps.societario.domain.services.processo_service import ProcessoService

from apps.societario.domain.entities.endereco import EnderecoEntity
from apps.societario.domain.entities.info_adicionais import InfoAdicionaisEntity
from apps.societario.domain.entities.formulario_abertura import FormularioAberturaEmpresaEntity

from apps.societario.infra.repositories.formulario_abertura_repository import FormularioAberturaRepository


class FormularioAberturaService(metaclass=ServiceBase):
    def __init__(
            self,
            repository=FormularioAberturaRepository(),
            processo_service=ProcessoService()
        ):

        self.__repository = repository
        self.__processo_service = processo_service
    
    def create_form(self, **data) -> FormularioAberturaEmpresaEntity:
        processo_id = data.pop('processo_id')

        processo = self.__processo_service.get_processo(processo_id)
        data['processo'] = processo

        endereco = EnderecoEntity(**data['endereco'])
        data['endereco'] = endereco

        info_adicionais = InfoAdicionaisEntity(**data['info_adicionais'])
        data['info_adicionais'] = info_adicionais

        response = FormularioAberturaEmpresaEntity(**data)

        self.__repository.create(response)
        
        return response
    
    def get_form(self, id: uuid.UUID) -> FormularioAberturaEmpresaEntity:
        if not id:
            raise ValidationError({'form_id': ['Parâmetro obrigatório.']})
        
        form = self.__repository.get_by_id(id)
        if not form:
            raise NotFound('Formulário não encontrado.')
        
        return FormularioAberturaEmpresaEntity(
            id=form.id,
            processo=form.processo,
            opcoes_nome_empresa=form.opcoes_nome_empresa,
            nome_fantasia=form.nome_fantasia,
            endereco=form.endereco,
            inscricao_imob=form.inscricao_imob,
            telefone=form.telefone,
            email=form.email,
            val_capital_social=form.val_capital_social,
            capital_integralizado=form.capital_integralizado,
            data_integralizacao=form.data_integralizacao,
            empresa_anexa_resid=form.empresa_anexa_resid,
            endereco_apenas_contato=form.endereco_apenas_contato,
            area_empresa=form.area_empresa,
            info_adicionais=form.info_adicionais,
            socios=form.socios,
            created_at=form.created_at,
            updated_at=form.updated_at
        )