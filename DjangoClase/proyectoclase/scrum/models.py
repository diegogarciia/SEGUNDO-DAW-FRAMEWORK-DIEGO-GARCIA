from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    dificultad = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre}"
