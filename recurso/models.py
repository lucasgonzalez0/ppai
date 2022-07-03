from ast import Raise
from re import A
from django.db import models
from PIL import Image

class GestorIngresoMantenimiento():
    fecha = ''
    reurso_seleccionado = ''
    personalCientifico = ''
    def __init__(self) -> None:
        pass

    def verificarTurno(self):
        self.personalCientifico.verificarTurno(recurso = self.reurso_seleccionado, fecha = self.fecha )

    

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

class CambioEstadoRT(models.Model):
    fechaHoraDesde = models.DateTimeField(null = True)
    fechaHoraHasta = models.DateTimeField(null = True, blank=True)
    estado = models.ForeignKey(Estado, on_delete = models.PROTECT)

    
    class Meta:
        verbose_name_plural = "CambiosEstadosRT"

    def __str__(self):
        return '{}-{}'.format(self.fechaHoraDesde,self.estado.nombre)
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

    def getNombreModelo(self):
        return self.marca

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
    turnos = models.ForeignKey(TipoRecursoTecnologico, on_delete = models.PROTECT, null = True, related_name='tipo_recurso')




   
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
        pass
    def nuevoMantenimientoPreventivo():
        pass
    def misTurnosDisponibles(self):
        #Buscar mis turnos disponibles
        mis_turnos = self.turnos.all()
        turnos_disponibles = []
        if mis_turnos:
            for turno in mis_turnos:
                if turno.esDisponible:
                    turnos_disponibles.append(turno)

        else:
            return turnos_disponibles
       
        
        
        


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