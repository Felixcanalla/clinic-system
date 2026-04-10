from django.conf import settings
from django.db import models


class Turno(models.Model):
    class Estado(models.TextChoices):
        RESERVADO = 'reservado', 'Reservado'
        CONFIRMADO = 'confirmado', 'Confirmado'
        EN_ESPERA = 'en_espera', 'En espera'
        ATENDIDO = 'atendido', 'Atendido'
        CANCELADO = 'cancelado', 'Cancelado'
        AUSENTE = 'ausente', 'Ausente'

    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.PROTECT,
        related_name='turnos'
    )
    profesional = models.ForeignKey(
        'profesionales.Profesional',
        on_delete=models.PROTECT,
        related_name='turnos'
    )

    fecha = models.DateField()
    hora = models.TimeField()

    motivo = models.CharField(max_length=255, blank=True)
    observaciones = models.TextField(blank=True)

    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.RESERVADO
    )

    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='turnos_creados'
    )

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['fecha', 'hora']
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        constraints = [
            models.UniqueConstraint(
                fields=['profesional', 'fecha', 'hora'],
                name='turno_unico_por_profesional_fecha_hora'
            )
        ]

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.paciente} con {self.profesional}"