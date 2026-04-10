from django.contrib import admin
from .models import Turno


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = (
        'fecha',
        'hora',
        'paciente',
        'profesional',
        'estado',
    )
    search_fields = (
        'paciente__apellido',
        'paciente__nombre',
        'paciente__documento',
        'profesional__apellido',
        'profesional__nombre',
        'motivo',
    )
    list_filter = (
        'estado',
        'fecha',
        'profesional',
    )