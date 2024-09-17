from apps.contabilidades.models import Contabilidade


class ContRepository:
    def create(self, **validated_data):
        contabilidade = Contabilidade(**validated_data)
        contabilidade.save()

        return contabilidade
    
    def is_cont_exists(self, cnpj):
        return Contabilidade.objects.filter(cnpj=cnpj).exists()