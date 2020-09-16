from django.db import models
from stdimage.models import StdImageField

class Ponto(models.Model):
    AVES = [
        ('SIM', 'SIM'),
        ('NÃO', 'NÃO')
    ]
    data = models.CharField("Data", max_length=30)
    matricula = models.CharField("Matrícula", max_length=10)
    aves = models.CharField('Aves?', choices=AVES, max_length=4)
    foto = StdImageField(upload_to='media')      
