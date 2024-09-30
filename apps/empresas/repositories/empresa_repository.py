from apps.empresas.models import Empresa


class EmpresaRepository:
    def create(self, **validated_data):
        empresa = Empresa(**validated_data)
        empresa.save()

        return empresa
    
    def is_empresa_exists(self, cnpj):
        return Empresa.objects.filter(cnpj=cnpj).exists()