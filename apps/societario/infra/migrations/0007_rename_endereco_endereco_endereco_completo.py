# Generated by Django 5.1.1 on 2024-11-19 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('societario', '0006_socios_created_at_socios_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endereco',
            old_name='endereco',
            new_name='endereco_completo',
        ),
    ]
