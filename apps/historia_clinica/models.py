from django.conf import settings
from django.db import models


class Consulta(models.Model):
    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.PROTECT,
        related_name='consultas'
    )
    profesional = models.ForeignKey(
        'profesionales.Profesional',
        on_delete=models.PROTECT,
        related_name='consultas'
    )
    turno = models.OneToOneField(
        'turnos.Turno',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='consulta'
    )

    fecha = models.DateField()
    hora = models.TimeField()

    motivo_consulta = models.CharField(max_length=255, blank=True)
    evolucion = models.TextField(blank=True)
    diagnostico = models.TextField(blank=True)
    plan = models.TextField(blank=True)
    indicaciones = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)

    creada_por = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='consultas_creadas'
    )

    creada_en = models.DateTimeField(auto_now_add=True)
    actualizada_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha', '-hora']
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return f"{self.fecha} {self.hora} - {self.paciente} - {self.profesional}"


class OrdenLaboratorio(models.Model):
    class Estado(models.TextChoices):
        SOLICITADA = 'solicitada', 'Solicitada'
        EN_PROCESO = 'en_proceso', 'En proceso'
        INFORMADA = 'informada', 'Informada'
        CANCELADA = 'cancelada', 'Cancelada'

    consulta = models.ForeignKey(
        Consulta,
        on_delete=models.CASCADE,
        related_name='ordenes_laboratorio'
    )
    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.PROTECT,
        related_name='ordenes_laboratorio'
    )
    profesional = models.ForeignKey(
        'profesionales.Profesional',
        on_delete=models.PROTECT,
        related_name='ordenes_laboratorio_emitidas'
    )

    fecha = models.DateField()
    practica = models.CharField(max_length=255)
    indicaciones = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.SOLICITADA
    )

    creada_en = models.DateTimeField(auto_now_add=True)
    actualizada_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha', '-id']
        verbose_name = 'Orden de laboratorio'
        verbose_name_plural = 'Órdenes de laboratorio'

    def __str__(self):
        return f"Lab: {self.practica} - {self.paciente} - {self.fecha}"



class ResultadoLaboratorio(models.Model):
    orden = models.OneToOneField(
        OrdenLaboratorio,
        on_delete=models.CASCADE,
        related_name='resultado'
    )

    fecha_resultado = models.DateField()
    observaciones = models.TextField(blank=True)

    informado_por = models.ForeignKey(
        'profesionales.Profesional',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='resultados_laboratorio'
    )

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Resultado de laboratorio'
        verbose_name_plural = 'Resultados de laboratorio'

    def __str__(self):
        return f"Resultado - {self.orden}"




class ItemResultadoLaboratorio(models.Model):
    resultado = models.ForeignKey(
        ResultadoLaboratorio,
        on_delete=models.CASCADE,
        related_name='items'
    )

    nombre = models.CharField(max_length=150)
    valor = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50, blank=True)
    valor_referencia = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = 'Ítem de resultado'
        verbose_name_plural = 'Ítems de resultado'

    def __str__(self):
        return f"{self.nombre}: {self.valor}"


class OrdenImagen(models.Model):
    class Estado(models.TextChoices):
        SOLICITADA = 'solicitada', 'Solicitada'
        EN_PROCESO = 'en_proceso', 'En proceso'
        INFORMADA = 'informada', 'Informada'
        CANCELADA = 'cancelada', 'Cancelada'

    consulta = models.ForeignKey(
        Consulta,
        on_delete=models.CASCADE,
        related_name='ordenes_imagen'
    )
    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.PROTECT,
        related_name='ordenes_imagen'
    )
    profesional = models.ForeignKey(
        'profesionales.Profesional',
        on_delete=models.PROTECT,
        related_name='ordenes_imagen_emitidas'
    )

    fecha = models.DateField()
    estudio = models.CharField(max_length=255)
    motivo = models.CharField(max_length=255, blank=True)
    observaciones = models.TextField(blank=True)
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.SOLICITADA
    )

    creada_en = models.DateTimeField(auto_now_add=True)
    actualizada_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fecha', '-id']
        verbose_name = 'Orden de imagen'
        verbose_name_plural = 'Órdenes de imágenes'

    def __str__(self):
        return f"Img: {self.estudio} - {self.paciente} - {self.fecha}"