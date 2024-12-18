import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField

from rest_framework.exceptions import ValidationError

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

class Endereco(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    endereco = models.CharField(max_length=255)
    complemento = models.CharField(max_length=150)
    endereco_completo = models.CharField(max_length=255)
    complemento = models.CharField(max_length=80)
    cep = models.CharField(max_length=9)

class InfoAdic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    resp_tecnica = models.BooleanField(default=False)
    nome_reponsavel = models.CharField(max_length=80, blank=True, null=True)

    nmr_carteira_profissional = models.CharField(max_length=11, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)

    area_resp = models.CharField(max_length=50, blank=True, null=True)

class FormularioAbertura(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    processo = models.OneToOneField(Processo, on_delete=models.CASCADE, related_name='formulario')
    opcoes_nome_empresa = ArrayField(models.CharField(max_length=120))
    nome_fantasia = models.CharField(max_length=120)

    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    inscricao_imob = models.CharField(max_length=20)

    telefone = models.CharField(max_length=12)
    email = models.EmailField(unique=False)

    val_capital_social = models.DecimalField(max_digits=10, decimal_places=2)
    capital_integralizado = models.BooleanField(default=False)
    data_integralizacao = models.DateField(blank=True, null=True)

    area_empresa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    empresa_anexa_resid = models.BooleanField(default=False)
    endereco_apenas_contato = models.BooleanField(default=False)

    info_adic = models.OneToOneField(InfoAdic, on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def clean(self):
        if len(self.opcoes_nomes_empresa) > 3:
            raise ValidationError('Você só pode adicionar até 3 nomes.')
        
        if not self.capital_integralizado and not self.data_integralizacao:
            raise ValidationError('O campo "data_integralizacao" é obrigatório quando a empresa não possui capital totalmente integralizado.')
        
        if not self.endereco_apenas_contato and not self.area_empresa:
            raise ValidationError('O campo "area_empresa" é obrigatório quando o endereço não é apenas para contato.')