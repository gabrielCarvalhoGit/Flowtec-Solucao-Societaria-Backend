import uuid
from django.db import models

from apps.contabilidades.models import Contabilidade


class AberturaEmpresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contabilidade = models.ForeignKey(Contabilidade, on_delete=models.CASCADE)

    nome_primario = models.CharField(max_length=100)
    nome_secundario = models.CharField(max_length=100, blank=True, null=True)
    nome_terciario = models.CharField(max_length=100, blank=True, null=True)

    cep = models.CharField(max_length=9, blank=True, null=True)
    endereco = models.CharField(max_length=150, blank=True, null=True)

    telefone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(unique=False, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nome_primario} - {self.contabilidade.nome}'