from django.contrib import admin
from .models import (
    Consulta,
    OrdenLaboratorio,
    OrdenImagen,
    ResultadoLaboratorio,
    ItemResultadoLaboratorio,
)


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = (
        'fecha',
        'hora',
        'paciente',
        'profesional',
        'turno',
    )
    search_fields = (
        'paciente__apellido',
        'paciente__nombre',
        'paciente__documento',
        'profesional__apellido',
        'profesional__nombre',
        'motivo_consulta',
        'diagnostico',
    )
    list_filter = (
        'fecha',
        'profesional',
    )


@admin.register(OrdenLaboratorio)
class OrdenLaboratorioAdmin(admin.ModelAdmin):
    list_display = (
        'fecha',
        'paciente',
        'practica',
        'profesional',
        'estado',
    )
    search_fields = (
        'paciente__apellido',
        'paciente__nombre',
        'paciente__documento',
        'practica',
        'profesional__apellido',
        'profesional__nombre',
    )
    list_filter = (
        'estado',
        'fecha',
        'profesional',
    )


# 🔥 INLINE (clave para laboratorio real)
class ItemResultadoLaboratorioInline(admin.TabularInline):
    model = ItemResultadoLaboratorio
    extra = 1


@admin.register(ResultadoLaboratorio)
class ResultadoLaboratorioAdmin(admin.ModelAdmin):
    list_display = (
        'orden',
        'fecha_resultado',
        'informado_por',
    )
    search_fields = (
        'orden__paciente__apellido',
        'orden__paciente__nombre',
        'orden__paciente__documento',
        'orden__practica',
    )
    inlines = [ItemResultadoLaboratorioInline]


@admin.register(OrdenImagen)
class OrdenImagenAdmin(admin.ModelAdmin):
    list_display = (
        'fecha',
        'paciente',
        'estudio',
        'profesional',
        'estado',
    )
    search_fields = (
        'paciente__apellido',
        'paciente__nombre',
        'paciente__documento',
        'estudio',
        'profesional__apellido',
        'profesional__nombre',
    )
    list_filter = (
        'estado',
        'fecha',
        'profesional',
    )