from django.contrib import admin

from recurso.models import CambioEstadoRT, Estado, Imagen, Modelo, RecursoTecnologico, Marca, TipoRecursoTecnologico

# Register your models here.

class ImagenAdmin(admin.StackedInline):
    model = Imagen

class RecursoTecnologicoAdmin(admin.ModelAdmin):
    inlines = [ImagenAdmin]

    class Meta:
        model = RecursoTecnologico



admin.site.register(Imagen)
admin.site.register(RecursoTecnologico)
# admin.site.register(RecursoTecnologicoAdmin)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Estado)
admin.site.register(CambioEstadoRT)
admin.site.register(TipoRecursoTecnologico)



