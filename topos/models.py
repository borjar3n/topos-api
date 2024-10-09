from django.db import models

# Create your models here.

from django.db import models

class Topo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    color = models.CharField(max_length=50)
    tamaño = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_encontrado = models.DateField()

    def __str__(self):
        return self.nombre

