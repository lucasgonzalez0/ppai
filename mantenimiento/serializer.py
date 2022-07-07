
from mantenimiento.models import Turno
from recurso.models import Estado, Marca, Modelo, RecursoTecnologico, TipoRecursoTecnologico
from rest_framework import serializers

from recurso.serializers import RecursoTecnologicoSerializer


    

class TurnoSerializer(serializers.ModelSerializer):
    # recurso = RecursoTecnologicoSerializer(many=True)


    class Meta:
        model = Turno
        fields = '__all__'

#    fechaGeneracion = models.DateTimeField(auto_now_add=True)
#     diaSemana = models.CharField(max_length = 20)
#     actual = models.ForeignKey(CambioEstadoTurno, on_delete = models.PROTECT, null = True, related_name='estado_turno_actual')
#     cambioEstadoTurno = models.ForeignKey(CambioEstadoTurno, on_delete = models.PROTECT, null = True, related_name='cambio_estado_Turno')
#     fechaHoraInicio = models.DateTimeField(null = True)
#     fechaHoraFin = models.DateTimeField(null = True, blank=True)
#     recurso = models.ForeignKey('recurso.RecursoTecnologico', on_delete = models.PROTECT, null = True, blank=True, related_name='turno')
#     asignacion = models.ForeignKey('personal.AsignacionResponsableTecnicoRT', on_delete = models.PROTECT, null = True, blank=True, related_name='turno')

    