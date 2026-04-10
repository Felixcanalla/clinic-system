from django.conf import settings
from django.db import models


class Profesional(models.Model):
    class Especialidad(models.TextChoices):
        CLINICA_MEDICA = 'clinica_medica', 'Clínica médica'
        PEDIATRIA = 'pediatria', 'Pediatría'
        CARDIOLOGIA = 'cardiologia', 'Cardiología'
        GINECOLOGIA = 'ginecologia', 'Ginecología'
        TRAUMATOLOGIA = 'traumatologia', 'Traumatología'
        DIAGNOSTICO_IMAGENES = 'diagnostico_imagenes', 'Diagnóstico por imágenes'
        BIOQUIMICA = 'bioquimica', 'Bioquímica'
        ENFERMERIA = 'enfermeria', 'Enfermería'
        FARMACIA = 'farmacia', 'Farmacia'
        OTRA = 'otra', 'Otra'

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='perfil_profesional'
    )

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    matricula = models.CharField(max_length=50, blank=True)
    especialidad = models.CharField(
        max_length=50,
        choices=Especialidad.choices,
        default=Especialidad.OTRA
    )

    telefono = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)

    activo = models.BooleanField(default=True)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name = 'Profesional'
        verbose_name_plural = 'Profesionales'

    def __str__(self):
        return f"{self.apellido}, {self.nombre} - {self.get_especialidad_display()}"