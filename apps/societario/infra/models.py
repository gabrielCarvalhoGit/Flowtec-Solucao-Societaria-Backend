import uuid
from django.db import models

from apps.contabilidades.models import Contabilidade


class Etapa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    nome = models.CharField(max_length=20)
    ordem = models.IntegerField()

class TipoProcesso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=37)

class Processo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    contabilidade = models.ForeignKey(Contabilidade, on_delete=models.CASCADE, related_name='processos')
    nome = models.CharField(max_length=80)

    tipo_processo = models.ForeignKey(TipoProcesso, on_delete=models.PROTECT, related_name='processos')
    etapa = models.ForeignKey(Etapa, on_delete=models.PROTECT, related_name='processos')
    
    created_at = models.DateTimeField(auto_now_add=True)
    expire_at = models.DateField()

class Tarefa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    descricao = models.CharField(max_length=80)
    etapa = models.ForeignKey(Etapa, on_delete=models.PROTECT, related_name='tarefas')
    ordem = models.IntegerField()
    obrigatoria = models.BooleanField(default=True)

class StatusTarefa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    processo = models.ForeignKey(Processo, on_delete=models.PROTECT, related_name='status_tarefa')
    etapa = models.ForeignKey(Etapa, on_delete=models.PROTECT, related_name='etapa')
    tarefa = models.ForeignKey(Tarefa, on_delete=models.PROTECT, related_name='status_tarefas')
    concluida = models.BooleanField(default=False)
    sequencia = models.IntegerField()

    updated_at = models.DateTimeField(auto_now=True)