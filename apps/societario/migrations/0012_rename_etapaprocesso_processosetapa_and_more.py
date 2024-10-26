# Generated by Django 5.1.1 on 2024-10-25 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societario', '0011_infoadic_remove_aberturaempresa_cep_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EtapaProcesso',
            new_name='ProcessosEtapa',
        ),
        migrations.AddField(
            model_name='aberturaempresa',
            name='area_empresa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='aberturaempresa',
            name='capital_integralizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aberturaempresa',
            name='data_integralizacao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aberturaempresa',
            name='empresa_anexa_resid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aberturaempresa',
            name='endereco_apenas_contato',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='aberturaempresa',
            name='info_adic',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societario.infoadic'),
        ),
        migrations.AddField(
            model_name='aberturaempresa',
            name='inscricao_imob',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='aberturaempresa',
            name='nome_fantasia',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='aberturaempresa',
            name='val_capital_social',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='aberturaempresa',
            name='endereco',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='societario.endereco'),
        ),
    ]
