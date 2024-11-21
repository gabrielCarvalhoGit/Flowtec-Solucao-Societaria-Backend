from rest_framework import serializers
from apps.societario.infra.models import InfoAdic


class InfoAdicResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoAdic
        fields = ['resp_tecnica', 'nome_reponsavel', 'nmr_carteira_profissional', 'uf', 'area_resp']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        null_fields = [key for key, value in representation.items() if not value and key != 'resp_tecnica']
        for key in null_fields:
            representation.pop(key)

        return representation