# Generated by Django 2.0.1 on 2018-03-19 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0006_auto_20180319_1419'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venda',
            options={'permissions': (('setar_nfe', 'Usuario pode alterar parametro NF-e'), ('ver_dashboard', 'Pode visualizar o Dashboard'), ('permissao3', 'Permissao 3'))},
        ),
    ]
