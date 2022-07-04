from django.urls import path,include
from rest_framework.routers import SimpleRouter
from recurso import views

app_name="recursos"
router = SimpleRouter()

router.register('recurso', views.RecursoTecnologicoViewSet, basename='recurso')

router.register('estado', views.EstadoViewSet, basename='estado')
router.register('marca', views.MarcaViewSet, basename='marca')
router.register('modelo', views.ModeloViewSet, basename='modelo')



urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    path('disponibles', views.RecursoTecnologicoDisponible.as_view(),name="recursos_disponibles"),
    path('verificarTurno', views.VerificarTurnoDisponible.as_view(),name="verificar_turno_dusasfas"),
]