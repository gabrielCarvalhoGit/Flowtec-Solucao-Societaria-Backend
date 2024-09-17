import uuid
from django.db import models


class Contabilidade(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    cnpj = models.CharField(max_length=14, unique=True)
    abertura = models.DateField()
    situacao = models.CharField(max_length=15)
    tipo = models.CharField(max_length=15)
    nome = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100, null=True, blank=True)
    porte = models.CharField(max_length=100)
    natureza_juridica = models.CharField(max_length=100)

    cod_atividade_principal = models.CharField(max_length=20)
    desc_atividade_principal = models.CharField(max_length=100)

    endereco = models.CharField(max_length=200)
    cep = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome