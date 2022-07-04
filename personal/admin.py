from django.contrib import admin

from personal.models import AsignacionResponsableTecnicoRT, PersonalCientifico

# Register your models here.
admin.site.register(PersonalCientifico)
admin.site.register(AsignacionResponsableTecnicoRT)