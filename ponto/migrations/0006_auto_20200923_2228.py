# Generated by Django 2.2.1 on 2020-09-24 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0005_auto_20200923_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ponto',
            name='latitude',
            field=models.CharField(max_length=30, verbose_name='Latitude'),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='longitude',
            field=models.CharField(max_length=30, verbose_name='Longitude'),
        ),
    ]
