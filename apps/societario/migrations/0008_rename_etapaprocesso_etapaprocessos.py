# Generated by Django 5.1.1 on 2024-10-22 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('societario', '0007_rename_nome_processo_aberturaempresa_nome'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EtapaProcesso',
            new_name='EtapaProcessos',
        ),
    ]
