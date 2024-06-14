from django.db import models

# Create your models here.
class Alumnos(models.Model):
    matricula = models.CharField(max_length=12,verbose_name="Mat")
    nombre = models.TextField()
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creaacion")
    update = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de actualizacion")

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]

    def __str__(self):
        return self.nombre