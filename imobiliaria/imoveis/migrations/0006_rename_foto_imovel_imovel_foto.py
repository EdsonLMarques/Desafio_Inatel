# Generated by Django 3.2.9 on 2022-01-07 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0005_imovel_foto_imovel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imovel',
            old_name='foto_imovel',
            new_name='foto',
        ),
    ]
