from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    class Roles(models.TextChoices):
        ADMINISTRADOR = 'administrador', 'Administrador'
        RECEPCION = 'recepcion', 'Recepción'
        MEDICO = 'medico', 'Médico'
        BIOQUIMICO = 'bioquimico', 'Bioquímico'
        TECNICO_IMAGENES = 'tecnico_imagenes', 'Técnico de Imágenes'
        FARMACIA = 'farmacia', 'Farmacia'
        ENFERMERIA = 'enfermeria', 'Enfermería'
        ADMINISTRACION = 'administracion', 'Administración'
        SUPERVISOR = 'supervisor', 'Supervisor'

    rol = models.CharField(
        max_length=30,
        choices=Roles.choices,
        default=Roles.RECEPCION
    )
    telefono = models.CharField(max_length=30, blank=True)
    documento = models.CharField(max_length=20, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.username} - {self.get_rol_display()}"