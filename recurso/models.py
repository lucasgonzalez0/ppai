from ast import Raise
from re import A
from django.db import models
from PIL import Image
from mantenimiento.models import Turno

from personal.models import AsignacionResponsableTecnicoRT, PersonalCientifico

class GestorIngresoMantenimiento():
    fecha = None
    fechaHoraActual = None
    reurso_seleccionado = ''
    usuario = 1
    personalCientifico = 1
    turnos = []
    asignacion_actual = None
    recursos_disponibles = [] 

    recursos_disponibles_datos = []
    def __init__(self) -> None:
        pass
    # Paso 1
    def agruparRTPorTipoDeRecurso():
        #Implementar
        pass
    def buscarRT(self):
        asignaciones = AsignacionResponsableTecnicoRT.objects.all()
        
        for asignacion in asignaciones:
            if asignacion.esPersonalCientificoLogueado():
                self.asignacion_actual = asignacion
        if self.asignacion_actual:
            self.recursos_disponibles = self.asignacion_actual.buscarRTDisponible()
        if self.recursos_disponibles:
            for recurso in self.recursos_disponibles:
                self.recursos_disponibles_datos.append(recurso.getDatos())
        if self.recursos_disponibles_datos:
            self.agruparRTPorTipoDeRecurso()


    def verificarTurno(self):
        recurso = RecursoTecnologico.objects.get(pk=1)
        personal = PersonalCientifico.objects.get(pk=1) # borrar
        turnos_recurso = personal.obtenerTurnosRecurso(recurso)
        if len(self.turnos):
            self.fechaHoraActual = ''
            #LOOP
            for turno in turnos_recurso:
                if turno.dentroFechaMantenimiento():
                    if turno.estado.esReservable():
                        pass


    

class Estado(models.Model):
    nombre = models.CharField(max_length = 500)
    descripcion = models.CharField(max_length = 500)
    ambito = models.CharField(max_length = 50,default = '')
    esCancelable = models.BooleanField(default = False)
    reservable = models.BooleanField(default = False)

    class Meta:
        verbose_name_plural = "Estados"

    def __str__(self):
        return '{}'.format(self.nombre)
    def crear():
        pass
    def mostrarEstado():
        pass
    def esReservable(self):
        return self.reservable
    def esAmbitoRT(self):
        return self.ambito == 'RT'
    def esDisponible(self):
        return self.nombre == 'Disponible'


class CambioEstadoRT(models.Model):
    fechaHoraDesde = models.DateTimeField(null = True)
    fechaHoraHasta = models.DateTimeField(null = True, blank=True)
    estado = models.ForeignKey(Estado, on_delete = models.PROTECT)

    
    class Meta:
        verbose_name_plural = "CambiosEstadosRT"

    def __str__(self):
        return '{}-{}'.format(self.fechaHoraDesde,self.estado.nombre)

    def esReservable(self):
        return self.estado.esReservable()

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
    turnos = models.ForeignKey(Turno, on_delete = models.PROTECT, null = True, blank=True, related_name='turno')
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
    def miModeloYMarca():
        return self.modelo.getNombreModelo()
    def nuevoMantenimientoPreventivo():
        pass
    def getTurnos(self):
        #Buscar mis turnos disponibles
        turnos = []
        for turno in self.turnos:
            turnos.append(turno.getDatos())
        return turnos

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