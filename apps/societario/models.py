import uuid
from django.db import models


class AberturaEmpresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    nome_primario = models.CharField(max_length=100)
    nome_secundario = models.CharField(max_length=100)
    nome_terciario = models.CharField(max_length=100)

    atividade_principal = models.CharField(max_length=150)

    cep = models.CharField(max_length=9)

    responsavel = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    telefone = models.CharField(max_length=12)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)