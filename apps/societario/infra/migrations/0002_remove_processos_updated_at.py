# Generated by Django 5.1.1 on 2024-12-02 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('societario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processos',
            name='updated_at',
        ),
    ]
