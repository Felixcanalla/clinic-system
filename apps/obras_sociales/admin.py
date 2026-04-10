from django.contrib import admin
from .models import ObraSocial, Plan, CoberturaPaciente


@admin.register(ObraSocial)
class ObraSocialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'activa')
    search_fields = ('nombre', 'codigo')
    list_filter = ('activa',)


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'obra_social', 'codigo', 'activo')
    search_fields = ('nombre', 'codigo', 'obra_social__nombre')
    list_filter = ('activo', 'obra_social')


@admin.register(CoberturaPaciente)
class CoberturaPacienteAdmin(admin.ModelAdmin):
    list_display = (
        'paciente',
        'obra_social',
        'plan',
        'numero_afiliado',
        'parentesco',
        'activa',
    )
    search_fields = (
        'paciente__apellido',
        'paciente__nombre',
        'paciente__documento',
        'numero_afiliado',
        'obra_social__nombre',
        'plan__nombre',
    )
    list_filter = ('activa', 'obra_social', 'parentesco')