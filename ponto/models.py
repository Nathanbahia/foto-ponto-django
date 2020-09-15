from django.db import models
from stdimage.models import StdImageField

class Ponto(models.Model):
    data = models.DateField("Data")
    nome = models.CharField("Nome", max_length=50)
    foto = StdImageField(upload_to='media')      
