from django.db import models


# Create your models here.
class Turno(models.Model):
    fechaGeneracion = models.DateTimeField(auto_now_add=True)
    diaSemana = models.CharField(max_length = 20)
    actual = models.ForeignKey('recurso.CambioEstadoRT', on_delete = models.PROTECT, null = True, related_name='estado_turno_actual')
    cambioEstadoTurno = models.ForeignKey('recurso.CambioEstadoRT', on_delete = models.PROTECT, null = True, related_name='cambio_estado_Turno')
    fechaHoraInicio = models.DateTimeField(null = True)
    fechaHoraFin = models.DateTimeField(null = True, blank=True)

    class Meta:
        verbose_name_plural = "Turnos"

    def __str__(self):
        return '{}-{}'.format(self.fechaGeneracion,self.fechaHoraInicio)

    def esDisponible(recurso, fecha):
        pass
    def getDatos(self):
        return self