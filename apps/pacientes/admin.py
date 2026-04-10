from django.contrib import admin
from .models import Paciente


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        'apellido',
        'nombre',
        'documento',
        'telefono',
        'localidad',
        'provincia',
        'activo',
    )
    search_fields = (
        'apellido',
        'nombre',
        'documento',
        'telefono',
        'localidad'
        'email',
    )
    list_filter = ('activo', 'sexo', 'localidad')