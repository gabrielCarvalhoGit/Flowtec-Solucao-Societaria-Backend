from rest_framework import serializers


class TarefaRequestSerializer(serializers.Serializer):
    tarefa_id = serializers.UUIDField(format='hex_verbose', write_only=True, required=True)
    concluida = serializers.BooleanField(required=True)

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
            
        return super().to_internal_value(data)

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