from django.contrib import admin
from .models import Profesional


@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = (
        'apellido',
        'nombre',
        'documento',
        'matricula',
        'especialidad',
        'activo',
    )
    search_fields = (
        'apellido',
        'nombre',
        'documento',
        'matricula',
        'email',
    )
    list_filter = ('especialidad', 'activo')