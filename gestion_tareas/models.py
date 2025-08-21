from django.db import models

# Modelo para tus tareas
class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

# Otro modelo de prueba
class AdlTest(models.Model):
    campo1 = models.CharField(max_length=100)
    valor1 = models.IntegerField()

    def __str__(self):
        return f"{self.campo1} - {self.valor1}"
