from apps.empresas.models import Empresa


class EmpresaRepository:
    def get_by_id(self, id):
        return Empresa.objects.get(id=id)
    
    def create(self, **validated_data):
        empresa = Empresa(**validated_data)
        empresa.save()

        return empresa
    
    # def create_empresa_process(self, **validated_data):
    #     empresa = AberturaEmpresa(**validated_data)
    #     empresa.save()

    #     return empresa
    
    def delete(self, empresa):
        empresa.delete()
    
    def is_empresa_exists(self, cnpj):
        return Empresa.objects.filter(cnpj=cnpj).exists()