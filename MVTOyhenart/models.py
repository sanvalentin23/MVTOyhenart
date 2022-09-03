from django.db import models

class Familiar(models.Model):
    nombre=models.CharField(max_length=150)
    edad=models.IntegerField()
    nacimiento=models.DateField()
