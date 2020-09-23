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
    foto = StdImageField("", upload_to='media', blank=True, null=True)    
