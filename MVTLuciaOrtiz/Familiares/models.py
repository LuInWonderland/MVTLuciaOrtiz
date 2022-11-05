from django.db import models

class Familiares(models.Model):
    nombre = models.CharField(max_length=40)
    dni = models.IntegerField()
    nacimiento = models.DateField()
