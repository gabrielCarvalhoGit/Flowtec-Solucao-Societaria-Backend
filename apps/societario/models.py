import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField

from apps.contabilidades.models import Contabilidade
from rest_framework.exceptions import ValidationError


class Etapas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_etapa = models.CharField(max_length=14)

class AberturaEmpresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    contabilidade = models.ForeignKey(Contabilidade, on_delete=models.CASCADE)
    etapa = models.ForeignKey(Etapas, on_delete=models.CASCADE)

    nome = models.CharField(max_length=100, unique=True)
    opcoes_nomes_empresa = ArrayField(models.CharField(max_length=250), blank=True, null=True)

    cep = models.CharField(max_length=9, blank=True, null=True)
    endereco = models.CharField(max_length=150, blank=True, null=True)

    telefone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(unique=False, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def clean(self):
        if self.nomes and len(self.nomes) > 3:
            raise ValidationError('Você só pode adicionar até 3 nomes.')
        
class NomeProcessos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_processo = models.CharField(max_length=80)
        
class Processos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    etapa = models.ForeignKey(Etapas, on_delete=models.CASCADE)
    empresa = models.ForeignKey(AberturaEmpresa, on_delete=models.CASCADE)
    nome_processo = models.ForeignKey(NomeProcessos, on_delete=models.CASCADE)

    status_processo = models.BooleanField(default=False)

class EtapaProcesso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    etapa = models.ForeignKey(Etapas, on_delete=models.CASCADE)
    nome_processo = models.ForeignKey(NomeProcessos, on_delete=models.CASCADE)