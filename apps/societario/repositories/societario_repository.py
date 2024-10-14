from apps.societario.models import AberturaEmpresa


class SocietarioRepository:
    def create(self, **validated_data):
        empresa = AberturaEmpresa(**validated_data)
        empresa.save()

        return empresa