import uuid
from django.db import models

from apps.core.models import BaseModel
from apps.contabilidades.models import Contabilidade


class AberturaEmpresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    nome_primario = models.CharField(max_length=100)
    nome_secundario = models.CharField(max_length=100)
    nome_terciario = models.CharField(max_length=100)

    atividade_principal = models.CharField(max_length=150)

    responsavel = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    telefone = models.CharField(max_length=12)

class Empresa(BaseModel):
    contabilidade = models.ForeignKey(Contabilidade, on_delete=models.CASCADE, null=True)
    abertura = models.ForeignKey(AberturaEmpresa, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome