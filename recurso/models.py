from ast import Raise
from re import A
from django.db import models
from PIL import Image
from mantenimiento.models import Mantenimiento, Turno
from datetime import date , datetime, tzinfo
from django.utils import timezone



from personal.models import AsignacionResponsableTecnicoRT, PersonalCientifico

class GestorIngresoMantenimiento():
    request = None
    fecha = None
    fechaFinMantenimiento = ''
    fechaHoraActual = None
    reurso_seleccionado = ''
    usuario = 1
    personalCientifico = 1
    turnos = []
    asignacion_actual = None
    recursos_disponibles = [] 
    estado_cancelado_turno = None
    estadoCanceladoPorMantenimientoCorrectivo = None

    recursos_disponibles_datos = []
    def __init__(self, request) -> None:
        self.request = request
        pass
    # Paso 1
    def agruparRTPorTipoDeRecurso(self,data):
        #Implementar

        order_list = data.sort(key=lambda x:x['cientifico'])
        print(order_list)
        print(type(order_list))
        for i in data:
            print(type(i))

        pass
    def buscarEstadoCanceladoPorMantenimiento(self):
        estados = Estado.objects.all()
        for estado in estados:
            if estado.esAmbitoTurno():
                if estado.esCanceladoPorMantenimientoCorrectivo():
                    return estado
    def buscarEstadoConIngresoEnMantenimientoCorrectivo(self):
        estados = Estado.objects.all()
        for estado in estados:
            if estado.esAmbitoRT():
                if estado.esConIngresoEnMantenimientoCorrectivo():
                    return estado
    def generarMantenimientoCorrectivo(self, recurso, turnos, estado_rt,estado_turno, motivo, fecha):
        personalCientifico = PersonalCientifico.objects.get(pk=1) # borrar
        personalCientifico.generarMantenimientoCorrectivo(recurso, turnos, estado_rt,estado_turno, motivo, fecha)

        # self.personalCientifico.generarMantenimientoCorrectivo(recurso, turnos, estado, motivo, fecha)
    def enviarNotificacionViaMail(self):
        enviado = True
        if enviado:
            return True
        
        
    def generarNotificacion(self):
        #TODO: Verificar personalCientifico
        personalCientifico = PersonalCientifico.objects.get(pk=1) # borrar

        email = personalCientifico.getMailCientifico()
        return self.enviarNotificacionViaMail()

    def tomarConfirmacionMantenimiento(self):
        #TODO: #Pasar por parametro los turnos devueltos
        self.motivo = self.request.data.get('motivo')
        self.reurso_seleccionado = self.request.data.get('recurso')
        recurso = RecursoTecnologico.objects.get(pk=self.reurso_seleccionado['id'])

        fecha = datetime.today()
        self.turnos = self.verificarTurno()
        self.estadoCanceladoPorMantenimientoCorrectivo = self.buscarEstadoCanceladoPorMantenimiento()
        estadoConIngresoEnMantenimientoCorrectivo = self.buscarEstadoConIngresoEnMantenimientoCorrectivo()
        self.generarMantenimientoCorrectivo(recurso, self.turnos, estadoConIngresoEnMantenimientoCorrectivo, self.estadoCanceladoPorMantenimientoCorrectivo, self.motivo, fecha)
        self.generarNotificacion()
        return 'Notificaciones enviadas'

    def buscarRT(self):
        asignaciones = AsignacionResponsableTecnicoRT.objects.all()
        
        for asignacion in asignaciones:
            if asignacion.esPersonalCientificoLogueado():
                self.asignacion_actual = asignacion
        if self.asignacion_actual:
            self.recursos_disponibles = self.asignacion_actual.buscarRTDisponible()
        if self.recursos_disponibles:
            datos_recurso = []
            for recurso in self.recursos_disponibles:
                #Agrupar por cientifico
                nombrecientifico_fechaInicioTurno_fechaFinTurno = self.recursos_disponibles_datos.append(recurso.getDatos())
        if self.recursos_disponibles_datos:
            self.agruparRTPorTipoDeRecurso()
    def getFechaHoraActual(self):
        self.fechaHoraActual = datetime.today()
        return self.fechaHoraActual

    def verificarTurno(self):
        fechaFinMantenimiento = self.request.data.get('fecha')
        fechaHoraActual = self.getFechaHoraActual()

        recurso = RecursoTecnologico.objects.get(pk=1)
        personal = PersonalCientifico.objects.get(pk=1) # borrar
        turnos_recurso = personal.obtenerTurnosRecurso(fechaHoraActual,fechaFinMantenimiento,recurso)
        return turnos_recurso
        
          
class Estado(models.Model):
    nombre = models.CharField(max_length = 500)
    descripcion = models.CharField(max_length = 500)
    ambito = models.CharField(max_length = 50,default = '')
    esCancelable = models.BooleanField(default = False)
    esReservable = models.BooleanField(default = False)

    class Meta:
        verbose_name_plural = "Estados"

    def __str__(self):
        return '{}'.format(self.nombre)
    def crear():
        pass
    def mostrarEstado():
        pass
    def esCanceladoPorMantenimientoCorrectivo(self):
        return self.nombre == 'Cancelado por mantenimiento correctivo'
    def esConIngresoEnMantenimientoCorrectivo(self):
        return self.nombre == 'Con ingreso mantenimiento correctivo'
    def esEstadoReservable(self):
        return self.esReservable
    def esAmbitoRT(self):
        return self.ambito == 'RT'
    def esAmbitoTurno(self):
        return self.ambito == 'TURNO'
    def esDisponible(self):
        return self.nombre == 'Disponible'
    def esConfirmadaOPendienteConfirmacion(self):
        return self.nombre == 'Confirmado' or self.nombre == 'Pendiente confirmacion'
class CambioEstadoRT(models.Model):
    fechaHoraDesde = models.DateTimeField(null = True)
    fechaHoraHasta = models.DateTimeField(null = True, blank=True)
    estado = models.ForeignKey(Estado, on_delete = models.PROTECT)

    class Meta:
        verbose_name_plural = "CambiosEstadosRT"

    def __str__(self):
        return '{}-{}'.format(self.fechaHoraDesde,self.estado.nombre)

    def esReservable(self):
        return self.estado.esEstadoReservable()

    def esAmbitoTurno(self):
        #Obtengo todos los estados
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

    def setFechaHoraHasta(self, fecha):
        self.fechaHoraHasta = fecha
        self.save()
    def esDisponible(self):

        estados = Estado.objects.all()
        estados_RT = []
        for estado in estados:
            if self.estado.esAmbitoRT():
                estados_RT.append(estado)
        
        estado_disponible = None
        for estado in estados_RT:
            if self.estado.esDisponible():
                estado_disponible = estado

        return self.estado == estado_disponible

class Marca(models.Model):
    nombre = models.CharField(max_length = 500)
    
    class Meta:
        verbose_name_plural = "Marcas"

    def __str__(self):
        return '{}'.format(self.nombre)
class Modelo(models.Model):
    nombre = models.CharField(max_length = 500)
    marca = models.ForeignKey(Marca, on_delete = models.PROTECT)

   
    class Meta:
        verbose_name_plural = "Modelos"

    def __str__(self):
        return '{}'.format(self.nombre)

    def getMarca():
        return self.marca.getNombre()

    def getNombreModelo(self):

        return self.nombre, self.getMarca()
class TipoRecursoTecnologico(models.Model):
    nombre = models.CharField(max_length = 50,null=True)
    descripcion = models.CharField(max_length = 150,null=True)

    class Meta:
        verbose_name_plural = "TipoRecursoTecnologico"

    def __str__(self):
        return '{}'.format(self.nombre)

    def crear():
        pass

    def mostrarCategoria():
        pass
    def getNombre(self):
        return self.nombre
    def conocerCategoria():
        pass
    def miModeloYMarca():
        pass
    def nuevoMantenimientoPreventivo():
        pass
    def misTurnosDisponibles():
        pass

class RecursoTecnologico(models.Model):
    numeroRT = models.IntegerField()
    fechaAlta = models.DateTimeField(auto_now_add=True)
    # perioricidadMatenimientoPrev
    # duracionMantenimientoPrev
    # fraccionHorariaTurno
    modelo = models.ForeignKey(Modelo, on_delete = models.PROTECT, null = True)
    actual = models.ForeignKey(CambioEstadoRT, on_delete = models.PROTECT, null = True, related_name='actual')
    cambioEstadoRT = models.ForeignKey(CambioEstadoRT, on_delete = models.PROTECT, null = True, related_name='cambioEstadoRT')
    tipoRecurso = models.ForeignKey(TipoRecursoTecnologico, on_delete = models.PROTECT, null = True, related_name='tipo_recurso')
    class Meta:
        verbose_name_plural = "RecursosTecnologicos"
    def __str__(self):
        return '{}'.format(self.numeroRT)
    def crear():
        pass
    def mostrarRT():
        pass
    def habilitar():
        pass
    def conocerCategoria():
        pass
    def miModeloYMarca(self):
        return self.modelo.getNombreModelo()
    def nuevoMantenimientoPreventivo(self,fechaInicio, motivo, recurso):
        mantenimiento = Mantenimiento(fechaHoraInicio=fechaInicio, motivoMantenimiento=motivo, recurso=recurso)
        mantenimiento.save()
        return
    def getTurnos(self, fechaHoraActual, fechaFinMantenimiento): # # El metodo debería ser mas especifico? Ej: getTurnosConfirmadosOPendientes
        #Buscar mis turnos disponibles
        turnos_recurso = []
        turnos = Turno.objects.all()
        for turno in turnos:
            if turno.esMiTurno(self):
                if turno.getDatos(fechaHoraActual, fechaFinMantenimiento):
                    turnos_recurso.append(turno.getDatos(fechaHoraActual, fechaFinMantenimiento))
        return turnos_recurso

        # return self.turnos.all() 
    def esRTDisponible(self):
        return self.actual.esDisponible()

    def getTipoRecurso(self):
        self.tipoRecurso.getNombre()

    def getNumeroRT(self):
        return self.numeroRT
    def getDatos(self):
        tipo_recurso_nombre = self.getTipoRecurso()
        numero_RT = self.getNumeroRT()
        modelo_nombre, marca_nombre = self.miModeloYMarca()
        return tipo_recurso_nombre, numero_RT, modelo_nombre, marca_nombre
    def obtenerEstadoActual(self, fecha): #No es el mejor nombre
        self.actual.setFechaHoraHasta(fecha)
    def crearCambioEstadoRT(self,estado, fecha):
        cambio_estado = CambioEstadoRT(fechaHoraDesde=fecha,estado=estado)
        cambio_estado.save()
        return
    def actualizarEstadoTurnos(self, turnos, estado_rt, estado_turno):
        fecha = datetime.today()
        for turno in turnos:
            turno = Turno.objects.get(pk=turno['id'])
            turno.actualizarEstado(estado_turno, fecha)
        self.obtenerEstadoActual(fecha)
        self.crearCambioEstadoRT(estado_rt,fecha)
    def generarMantenimientoCorrectivo(self,recurso, turnos,estado_rt, estado_turno, motivo, fecha):
        self.actualizarEstadoTurnos(turnos, estado_rt,estado_turno)
        self.nuevoMantenimientoPreventivo(fecha,motivo,recurso)

       
        
        
        


class Imagen(models.Model):
    rt = models.ForeignKey(RecursoTecnologico, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to ='imagenes/')

    # resizing the image, you can change parameters like size and quality.
    def save(self, *args, **kwargs):
       super(Imagen, self).save(*args, **kwargs)
       img = Image.open(self.photo.path)
       if img.height > 1125 or img.width > 1125:
           img.thumbnail((1125,1125))
       img.save(self.imagen.path,quality=70,optimize=True)