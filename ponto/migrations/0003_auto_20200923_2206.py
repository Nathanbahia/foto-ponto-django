# Generated by Django 2.2.1 on 2020-09-24 01:06

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0002_auto_20200916_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='ponto',
            name='latitude',
            field=models.CharField(default=1, max_length=30, verbose_name='Latitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ponto',
            name='longitude',
            field=models.CharField(default=1, max_length=30, verbose_name='Latitude'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ponto',
            name='aves',
            field=models.CharField(choices=[('SIM', 'Sim'), ('NÃO', 'Não')], max_length=4, verbose_name='Presença de aves no local?'),
        ),
        migrations.AlterField(
            model_name='ponto',
            name='foto',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='media', verbose_name=''),
        ),
    ]