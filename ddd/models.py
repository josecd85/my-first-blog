from django.db import models
from django.utils import timezone

# Create your models here.
class Alertas(models.Model):
    idAlert = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=25)
    descrip = models.CharField(max_length=100)
    estado = models.CharField(max_length=1)
    falta = models.DateTimeField(default=timezone.now)
    ffin = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return str(self.idAlert)+"-"+self.titulo