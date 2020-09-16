from django.db import models
from stdimage.models import StdImageField

class Ponto(models.Model):
    data = models.CharField("Data", max_length=30)
    nome = models.CharField("Nome", max_length=50)
    foto = StdImageField(upload_to='media')      
