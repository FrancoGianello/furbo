from django.db import models

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=200)
    escudo = models.FileField()

class Partido(models.Model):
    local = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    resultado = models.CharField("0-0", max_length=100)