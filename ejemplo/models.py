from django.db import models
from datetime import datetime



# Create your models here.
from django.db import models

class Familiar (models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    fecha_nacimiento = models.DateField("%d-%m-%y")



def __str__(self):
      return f"{self.nombre}, {self.numero_pasaporte}, {self.id}, {self.fecha_nacimiento}"
      
