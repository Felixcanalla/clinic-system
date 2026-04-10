from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {
            'fields': ('rol', 'telefono', 'documento', 'activo')
        }),
    )

    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'rol',
        'is_staff',
        'activo',
    )

    list_filter = ('rol', 'is_staff', 'is_superuser', 'activo')