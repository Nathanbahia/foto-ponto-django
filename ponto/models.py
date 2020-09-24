from django.db import models
from stdimage.models import StdImageField


class Ponto(models.Model):
    AVES = [
        ('SIM', 'Sim'),
        ('NÃO', 'Não')
    ]
    data = models.CharField("Data", max_length=30)
    matricula = models.CharField("Matrícula", max_length=10)
    aves = models.CharField('Presença de aves no local?', choices=AVES, max_length=4)
    foto = StdImageField("Foto", upload_to='media', blank=True, null=True)
    latitude = models.CharField("Latitude", max_length=30)
    longitude = models.CharField("Longitude", max_length=30)
