from rest_framework import serializers
from apps.societario.infra.models import AberturaEmpresa

from .endereco_response import EnderecoResponseSerializer
from .info_adic_response import InfoAdicResponseSerializer


class CreateProcessResponseSerializer(serializers.ModelSerializer):
    contabilidade = serializers.CharField(source='contabilidade.nome', read_only=True)
    
    class Meta:
        model = AberturaEmpresa
        fields = ['id', 'nome', 'contabilidade', 'expire_at', 'created_at']

class FormularioAberturaResponseSerializer(serializers.ModelSerializer):
    contabilidade = serializers.CharField(source='contabilidade.nome', read_only=True)
    endereco = EnderecoResponseSerializer(read_only=True)
    info_adic = InfoAdicResponseSerializer(read_only=True)

    class Meta:
        model = AberturaEmpresa
        fields = [
            'id', 'contabilidade',
            
            'opcoes_nomes_empresa', 'nome_fantasia', 'endereco', 'inscricao_imob',
            'telefone', 'email',
             
            'val_capital_social', 'capital_integralizado', 'data_integralizacao',


            'area_empresa', 'empresa_anexa_resid', 'endereco_apenas_contato', 'info_adic',

            'updated_at', 'expire_at'
        ]