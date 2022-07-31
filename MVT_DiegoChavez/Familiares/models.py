from django.db import models

# Create your models here.
class info_familiares(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento = models.IntegerField()
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=30)

