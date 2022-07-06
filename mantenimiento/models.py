from this import s
from django.db import models
from numpy import true_divide

from personal.models import AsignacionResponsableTecnicoRT
from datetime import datetime


# Create your models here.
class Turno(models.Model):
    fechaGeneracion = models.DateTimeField(auto_now_add=True)
    diaSemana = models.CharField(max_length = 20)
    actual = models.ForeignKey('recurso.CambioEstadoRT', on_delete = models.PROTECT, null = True, related_name='estado_turno_actual')
    cambioEstadoTurno = models.ForeignKey('recurso.CambioEstadoRT', on_delete = models.PROTECT, null = True, related_name='cambio_estado_Turno')
    fechaHoraInicio = models.DateTimeField(null = True)
    fechaHoraFin = models.DateTimeField(null = True, blank=True)
    recurso = models.ForeignKey('recurso.RecursoTecnologico', on_delete = models.PROTECT, null = True, blank=True, related_name='turno')
    asignacion = models.ForeignKey('personal.AsignacionResponsableTecnicoRT', on_delete = models.PROTECT, null = True, blank=True, related_name='turno')

    

    class Meta:
        verbose_name_plural = "Turnos"

    def __str__(self):
        return '{}-{}'.format(self.fechaGeneracion,self.fechaHoraInicio)

    def esDisponible(recurso, fecha):
        pass
    def dentro(recurso, fecha):
        pass
    def getFechaHoraInicio(self):
        return self.fechaHoraInicio

    def getFechaHoraFin(self):
        return self.fechaHoraFin
        
    def getCientificoAsignado(self):
        return self.asignacion.getCientificoAsignado()
        

    def getDatos(self, fechaHoraActual, fechaFinMantenimiento):
        #Verifico que el turno este dentro de la fecha de mantenimiento
        if self.dentroFechaMantenimiento(fechaHoraActual, fechaFinMantenimiento):
            #Verifico que el estado actual sea reservable
            if self.actual.esReservable():
                #Obtengo todos los estados el turno
                estados_del_turno = self.actual.esAmbitoTurno()
                #Obtengo los estados pendiente de confirmacion y confirmada
                estados_pendiente_o_confirmada = self.actual.esConfirmadaOPendienteConfirmacion(estados_del_turno)
               
                 
                #Obtengo todos los turnos con estado pendiente y confirmada
                turnos_confirmados_y_pendientes = []

                #TODO: Controlar
                for estado in estados_pendiente_o_confirmada:
                    if self.actual.estado == estado:
                        data = {}
                        data['fechaInicio'] = self.getFechaHoraInicio()
                        data['fechaFin'] = self.getFechaHoraFin()
                        data['cientifico'] = self.getCientificoAsignado()
                        return data
                return



                
        return self
    def esMiTurno(self, recurso):
        return self.recurso == recurso


    def dentroFechaMantenimiento(self,fechaHoraActual, fechaFinMantenimiento):

        fechaHoraInicio = self.fechaHoraInicio.strftime('%Y-%m-%d') # 07/05/2022
        fechaHoraInicio = datetime.strptime(fechaHoraInicio, '%Y-%m-%d') 
        print("fechaHoraInicio",fechaHoraInicio)


        fechaHoraActual = fechaHoraActual.strftime('%Y-%m-%d')
        fechaHoraActual = datetime.strptime(fechaHoraActual, '%Y-%m-%d') 
        print("fechaHoraActual",fechaHoraActual)

        print(type(fechaFinMantenimiento))
        fechaFinMantenimiento = datetime.strptime(fechaFinMantenimiento, '%Y-%m-%d')
        print("fechaFinMantenimiento",fechaFinMantenimiento)


        if fechaHoraInicio < fechaHoraActual:
            if fechaHoraInicio < fechaFinMantenimiento:
                return True
        return False
        # return self.fechaHoraInicio > fechaHoraActual and self.fechaHoraInicio <  datetime.strptime(fechaFinMantenimiento, '%Y-%m-%d') 