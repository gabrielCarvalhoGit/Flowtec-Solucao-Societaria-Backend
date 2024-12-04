import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField

from apps.contabilidades.models import Contabilidade


# class Etapa(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     nome_etapa = models.CharField(max_length=20)

# class Endereco(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#     endereco_completo = models.CharField(max_length=255)
#     complemento = models.CharField(max_length=80)
#     cep = models.CharField(max_length=9)

# class InfoAdic(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#     resp_tecnica = models.BooleanField(default=False)
#     nome_reponsavel = models.CharField(max_length=80, blank=True, null=True)

#     nmr_carteira_profissional = models.CharField(max_length=11, blank=True, null=True)
#     uf = models.CharField(max_length=2, blank=True, null=True)

#     area_resp = models.CharField(max_length=50, blank=True, null=True)

# class AberturaEmpresa(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     contabilidade = models.ForeignKey(Contabilidade, on_delete=models.CASCADE)
#     etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, blank=True, null=True)

#     nome = models.CharField(max_length=100)
#     opcoes_nomes_empresa = ArrayField(models.CharField(max_length=100), blank=True, null=True)
#     nome_fantasia = models.CharField(max_length=100, blank=True, null=True)

#     endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, blank=True, null=True)
#     inscricao_imob = models.CharField(max_length=20, blank=True, null=True)

#     telefone = models.CharField(max_length=12, blank=True, null=True)
#     email = models.EmailField(unique=False, blank=True, null=True)

#     val_capital_social = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     capital_integralizado = models.BooleanField(default=False)
#     data_integralizacao = models.DateField(blank=True, null=True)

#     area_empresa = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     empresa_anexa_resid = models.BooleanField(default=False)
#     endereco_apenas_contato = models.BooleanField(default=False)

#     info_adic = models.OneToOneField(InfoAdic, on_delete=models.CASCADE, blank=True, null=True)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     expire_at = models.DateField()

# class Socios(models.Model):
#     ESTADO_CIVIL_CHOICES = [
#         ('solteiro', 'Solteiro'),
#         ('casado', 'Casado'),
#         ('separado', 'Separado judicialmente'),
#         ('divorciado', 'Divorciado'),
#         ('viuvo', 'Viúvo')
#     ]

#     REGIME_CASAMENTO_CHOICES = [
#         ('separacao_total', 'Separação total de bens'),
#         ('comunhao_parcial', 'Comunhão parcial de bens'),
#         ('comunhao_universal', 'Comunhão universal de bens'),
#         ('participacao_final', 'Participação final nos aquestos')
#     ]

#     TIPO_ADMINISTRADOR_CHOICES = [
#         ('conjunto', 'Conjunto'),
#         ('isoladamente', 'Isoladamente'),
#         ('nao_aplica', 'Não se aplica')
#     ]

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     empresa = models.ForeignKey(AberturaEmpresa, on_delete=models.CASCADE)

#     nome = models.CharField(max_length=100)
#     nacionalidade = models.CharField(max_length=25)
#     data_nascimento = models.DateField()

#     estado_civil = models.CharField(max_length=10, choices=ESTADO_CIVIL_CHOICES)
#     regime_casamento = models.CharField(max_length=20, choices=REGIME_CASAMENTO_CHOICES, blank=True, null=True)

#     profissao = models.CharField(max_length=50)

#     cpf = models.CharField(max_length=11)
#     rg = models.CharField(max_length=14)
#     orgao_expedidor = models.CharField(max_length=8)
#     uf = models.CharField(max_length=2)

#     administrador = models.BooleanField(default=False)
#     tipo_administrador = models.CharField(max_length=15, choices=TIPO_ADMINISTRADOR_CHOICES)
    
#     qtd_cotas = models.IntegerField()
#     endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class NomeProcesso(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     nome_processo = models.CharField(max_length=80)

# class Processo(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#     etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
#     empresa = models.ForeignKey(AberturaEmpresa, on_delete=models.CASCADE)
#     nome_processo = models.ForeignKey(NomeProcesso, on_delete=models.CASCADE)

#     status_processo = models.BooleanField(default=False)

# class ProcessosEtapa(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

#     etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
#     nome_processo = models.ForeignKey(NomeProcesso, on_delete=models.CASCADE)


class Etapa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    nome = models.CharField(max_length=20)
    ordem = models.IntegerField()

class TipoProcesso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=37)

class Processo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    contabilidade = models.ForeignKey(Contabilidade, on_delete=models.CASCADE)
    nome = models.CharField(max_length=80)

    tipo_processo = models.ForeignKey(TipoProcesso, on_delete=models.PROTECT)
    etapa = models.ForeignKey(Etapa, on_delete=models.PROTECT, related_name='processos')
    
    expire_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Tarefa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    descricao = models.CharField(max_length=80)
    etapa = models.ForeignKey(Etapa, on_delete=models.PROTECT, related_name='tarefas')
    ordem = models.IntegerField()
    obrigatoria = models.BooleanField(default=True)

class StausTarefa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    processo = models.ForeignKey(Processo, on_delete=models.PROTECT, related_name='stats_tarefa')
    etapa = models.ForeignKey(Etapa, on_delete=models.PROTECT, related_name='etapa')
    tarefa = models.ForeignKey(Tarefa, on_delete=models.PROTECT, related_name='status_tarefas')
    concluida = models.BooleanField(default=False)
    sequencia = models.IntegerField()

    updated_at = models.DateTimeField(auto_now=True)