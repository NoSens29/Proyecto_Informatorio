from django.contrib import admin
from voluntariado.models import Persona, Actividad

# Register your models here.

admin.site.register(Persona)
admin.site.register(Actividad)


from django.contrib.auth.admin import UserAdmin

from voluntariado.forms import MiUsuarioCreationForm

from voluntariado.models import User


# Heredamos del UserAdmin original para usar nuestros formularios customizados
class MiUsuarioAdmin(UserAdmin):
    form = MiUsuarioCreationForm
    add_form = MiUsuarioCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (
            None, {
                'fields': (
                    'dni',
                    'voluntario',
                    'solicitante'
                )
            }
        ),
    )

'''
@admin.register(User)
class UserAdmin(MiUsuarioCreationForm):
    list_display =  (
        'id',
        'username',
        'password',
        'dni'
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'is_superuser',
        'voluntario',
        'solicitante',
        'last_login',
        'date_joined'
    )


@admin.register(PatientProfile)
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'active',
        'user_id'
    )


@admin.register(MedicalProfile)
class MedicalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'active',
        'user_id'
    )


@admin.register(PhysiotherapistProfile)
class PhysiotherapistAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'active',
        'user_id'
    )
   '''