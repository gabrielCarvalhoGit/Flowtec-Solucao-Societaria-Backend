from rest_framework import serializers
from apps.societario.infra.models import StatusTarefa


class TarefaRequestSerializer(serializers.Serializer):
    id = serializers.UUIDField(format='hex_verbose', write_only=True, required=True)
    concluida = serializers.BooleanField(required=True)
    nao_aplicavel = serializers.BooleanField(required=False, default=False)
    expire_at = serializers.DateField(required=False)
    tipo_tributacao = serializers.CharField(max_length=10, required=False, allow_blank=True)

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
        
        internal_data = super().to_internal_value(data)

        if internal_data.get('concluida') and internal_data.get('nao_aplicavel'):
            raise serializers.ValidationError({
                'nao_aplicavel': 'Uma tarefa não pode ser marcada como concluída e não aplicável simultaneamente.'
            })

        return internal_data


class StatusTarefaRequestSerializer(serializers.Serializer):
    processo_id = serializers.UUIDField(format='hex_verbose', write_only=True, required=True)
    etapa_id = serializers.UUIDField(format='hex_verbose', write_only=True, required=False)
    tarefas = TarefaRequestSerializer(many=True, required=True)

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
        
        internal_data = super().to_internal_value(data)

        tarefas = internal_data.get('tarefas')
        if not tarefas:
            raise serializers.ValidationError({'tarefas': 'Este campo não pode ser vazio.'})

        return internal_data