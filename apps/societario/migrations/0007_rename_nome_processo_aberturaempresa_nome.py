# Generated by Django 5.1.1 on 2024-10-19 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('societario', '0006_etapaprocesso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aberturaempresa',
            old_name='nome_processo',
            new_name='nome',
        ),
    ]
