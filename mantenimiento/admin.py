from django.contrib import admin

from mantenimiento.models import CambioEstadoTurno, Turno

# Register your models here.

admin.site.register(Turno)
admin.site.register(CambioEstadoTurno)
