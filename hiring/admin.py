from django.contrib import admin

# Register your models here.
from .models import (
    AreasConocimiento,
    Bancos,
    Universidades,
    Profesiones,
    Usuarios,
    Empresas,
    Postulantes,
    Vacantes,
    Postulaciones,
    Contratos,
    ExperienciasLaborales,
    Nominas,
    Recibos,
)

admin.site.register(AreasConocimiento)
admin.site.register(Bancos)
admin.site.register(Universidades)
admin.site.register(Profesiones)
admin.site.register(Usuarios)
admin.site.register(Empresas)
admin.site.register(Postulantes)
admin.site.register(Vacantes)
admin.site.register(Postulaciones)
admin.site.register(Contratos)
admin.site.register(ExperienciasLaborales)
admin.site.register(Nominas)
admin.site.register(Recibos)
