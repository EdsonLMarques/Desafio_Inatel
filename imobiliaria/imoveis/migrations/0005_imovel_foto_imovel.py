# Generated by Django 3.2.9 on 2022-01-05 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imoveis', '0004_rename_endereço_imovel_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='foto_imovel',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y'),
        ),
    ]
