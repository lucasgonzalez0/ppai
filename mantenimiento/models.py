from django.db import models
from numpy import true_divide

from personal.models import AsignacionResponsableTecnicoRT
from datetime import datetime
from django.apps import apps


# Create your models here.
class CambioEstadoTurno(models.Model):
    fechaHoraDesde = models.DateTimeField(null = True)
    fechaHoraHasta = models.DateTimeField(null = True, blank=True)
    estado = models.ForeignKey('recurso.Estado', on_delete = models.PROTECT)

    class Meta:
        verbose_name_plural = "CambiosEstadosTurno"

    def __str__(self):
        return '{}-{}'.format(self.fechaHoraDesde,self.estado.nombre)

    def esReservable(self):
        return self.estado.esEstadoReservable()
    def esAmbitoTurno(self):
        #Obtengo todos los estados
        Estado = apps.get_model('recurso','Estado')
        estados = Estado.objects.all()
        estados_turno = []
        #Para todos los estados, obtengo los de ambito turno.
        for estado in estados:
            if estado.esAmbitoTurno():
                estados_turno.append(estado)
        return estados_turno

    def esConfirmadaOPendienteConfirmacion(self, estados):
        estados_confirmado_o_pendiente = []
        for estado in estados:
            if estado.esConfirmadaOPendienteConfirmacion():
                estados_confirmado_o_pendiente.append(estado)
        return estados_confirmado_o_pendiente

    def setFechaHoraHasta(self,fecha):
        self.fechaHoraHasta = fecha
        self.save()
   

class Turno(models.Model):
    fechaGeneracion = models.DateTimeField(auto_now_add=True)
    diaSemana = models.CharField(max_length = 20)
    actual = models.ForeignKey(CambioEstadoTurno, on_delete = models.PROTECT, null = True, related_name='estado_turno_actual')
    cambioEstadoTurno = models.ForeignKey(CambioEstadoTurno, on_delete = models.PROTECT, null = True, related_name='cambio_estado_Turno')
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
    def crearCambioEstadoTurno(self, estado,fecha):
        cambio_estado = CambioEstadoTurno(fechaHoraDesde=fecha,estado=estado)
        cambio_estado.save()
        self.cambioEstadoTurno = self.actual
        self.actual = cambio_estado
        self.save()         
        return

    def actualizarEstado(self, estado, fecha):
        estado_actual = self.obtenerEstadoActual()
        estado_actual.setFechaHoraHasta(fecha)
        self.crearCambioEstadoTurno(estado,fecha)


    def obtenerEstadoActual(self):
        return self.actual

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

                for estado in estados_pendiente_o_confirmada:
                    if self.actual.estado == estado:
                        data = {}
                        data['id'] = self.pk

                        data['fechaInicio'] = self.getFechaHoraInicio()
                        data['fechaFin'] = self.getFechaHoraFin()
                        data['cientifico'] = self.getCientificoAsignado()
                        return data
                return



                
        return None
    def esMiTurno(self, recurso):
        return self.recurso == recurso

    def dentroFechaMantenimiento(self,fechaHoraActual, fechaFinMantenimiento):

        fechaHoraInicioDelTurno = self.fechaHoraInicio.strftime('%Y-%m-%d') # 07/05/2022
        fechaHoraInicioDelTurno = datetime.strptime(fechaHoraInicioDelTurno, '%Y-%m-%d') 
        print("fechaHoraInicio",fechaHoraInicioDelTurno)


        fechaHoraActual = fechaHoraActual.strftime('%Y-%m-%d')
        fechaHoraActual = datetime.strptime(fechaHoraActual, '%Y-%m-%d') 
        print("fechaHoraActual",fechaHoraActual)

        print(type(fechaFinMantenimiento))
        fechaFinMantenimiento = datetime.strptime(fechaFinMantenimiento, '%Y-%m-%d')
        print("fechaFinMantenimiento",fechaFinMantenimiento)


        if fechaHoraInicioDelTurno > fechaHoraActual:
            if fechaHoraInicioDelTurno < fechaFinMantenimiento:
                return True
        return False
        # return self.fechaHoraInicio > fechaHoraActual and self.fechaHoraInicio <  datetime.strptime(fechaFinMantenimiento, '%Y-%m-%d') 

class Mantenimiento(models.Model):
    fechaHoraInicio = models.DateTimeField(null = True)
    fechaHoraFin = models.DateTimeField(null = True, blank=True)
    fechaHoraInicioPrevista = models.DateTimeField(null = True)
    motivoMantenimiento = models.CharField(max_length = 500,null=True) # Hace falta especificar el mantenimiento al estar en la clase mantenimiento
    recurso = models.ForeignKey('recurso.RecursoTecnologico', on_delete = models.PROTECT, null = True, blank=True, related_name='recurso_mantenimiento')
    
    class Meta:
        verbose_name_plural = "Mantenimiento"

    def __str__(self):
        return '{}-{}'.format(self.fechaHoraInicio,self.fechaHoraFin)