from apps.contabilidades.models import Contabilidade


class ContRepository:
    def get_by_id(self, id):
        return Contabilidade.objects.get(id=id)
    
    def get_contabilidades(self):
        return Contabilidade.objects.all().order_by('-created_at')
        
    def create(self, **validated_data):
        contabilidade = Contabilidade(**validated_data)
        contabilidade.save()

        return contabilidade
    
    def delete(self, contabilidade):
        contabilidade.delete()
    
    def is_cont_exists(self, cnpj):
        return Contabilidade.objects.filter(cnpj=cnpj).exists()