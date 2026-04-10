from django.db import models


class ObraSocial(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    codigo = models.CharField(max_length=30, blank=True)
    activa = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Obra social'
        verbose_name_plural = 'Obras sociales'

    def __str__(self):
        return self.nombre


class Plan(models.Model):
    obra_social = models.ForeignKey(
        ObraSocial,
        on_delete=models.CASCADE,
        related_name='planes'
    )
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=30, blank=True)
    activo = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        ordering = ['obra_social__nombre', 'nombre']
        verbose_name = 'Plan'
        verbose_name_plural = 'Planes'
        unique_together = ('obra_social', 'nombre')

    def __str__(self):
        return f"{self.obra_social.nombre} - {self.nombre}"


class CoberturaPaciente(models.Model):
    class Parentesco(models.TextChoices):
        TITULAR = 'titular', 'Titular'
        CONYUGE = 'conyuge', 'Cónyuge'
        HIJO = 'hijo', 'Hijo/a'
        OTRO = 'otro', 'Otro'

    paciente = models.ForeignKey(
        'pacientes.Paciente',
        on_delete=models.CASCADE,
        related_name='coberturas'
    )
    obra_social = models.ForeignKey(
        ObraSocial,
        on_delete=models.PROTECT,
        related_name='coberturas_pacientes'
    )
    plan = models.ForeignKey(
        Plan,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='coberturas_pacientes'
    )

    numero_afiliado = models.CharField(max_length=50)
    titular = models.CharField(max_length=150, blank=True)
    parentesco = models.CharField(
        max_length=20,
        choices=Parentesco.choices,
        default=Parentesco.TITULAR
    )

    vigente_desde = models.DateField(null=True, blank=True)
    vigente_hasta = models.DateField(null=True, blank=True)

    activa = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True)

    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-activa', 'obra_social__nombre']
        verbose_name = 'Cobertura de paciente'
        verbose_name_plural = 'Coberturas de pacientes'

    def __str__(self):
        return f"{self.paciente} - {self.obra_social} - {self.numero_afiliado}"