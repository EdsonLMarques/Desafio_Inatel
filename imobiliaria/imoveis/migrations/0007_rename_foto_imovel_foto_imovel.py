# Generated by Django 3.2.9 on 2022-01-08 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0006_rename_foto_imovel_imovel_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imovel',
            old_name='foto',
            new_name='foto_imovel',
        ),
    ]
