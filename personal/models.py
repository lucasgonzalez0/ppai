from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _



class PersonalCientifico(models.Model):
    usuario = models.ForeignKey(User, null = True, on_delete = models.PROTECT)
    nombre = models.CharField(max_length = 50,null=True)
    apellido = models.CharField(max_length = 50,null=True)
    legajo = models.CharField(max_length = 50,null=True)
    correoElectronicoInstitucional = models.EmailField(null=True, blank=True)
    correoElectronicoPersonal = models.EmailField(null=True, blank=True)
    numeroDocumento = models.CharField(
        null=True, 
        blank=True,
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[0-9]{7,9}$',
                message=_('Por favor seleccione un número de documento válido.')
        )]
    )
    telefonoCelular = models.CharField(
        null=True, 
        blank=True,
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^[0-9]{7,10}$',
                message=_('Por favor seleccione un número de teléfono válido.')
        )]
    )
    fechaAlta = models.DateTimeField(auto_now_add=True)


   
    class Meta:
        verbose_name_plural = "PersonalCientifico"

    def __str__(self):
        return '{} - {}'.format(self.legajo, self.nombre)

    def crear():
        pass
    def mostrarPersonalCientifico():
        pass
    def inhabilitarUsuario():
        pass
    def habilitarUsuario():
        pass
    def tengoUsuarioHabilitado():
        pass
    def mostrarMisNovedades():
        pass
    def obtenerTurnosRecurso(self,fechaHoraActual,fechaFinMantenimiento,recurso):
        return recurso.getTurnos(fechaHoraActual, fechaFinMantenimiento)
    def getNombre(self):
        return self.nombre
    def generarMantenimientoCorrectivo(self,recurso, turnos, estado_rt,estado_turno, motivo, fecha):
        return recurso.generarMantenimientoCorrectivo(recurso,turnos, estado_rt,estado_turno, motivo, fecha)
    def getMailCientifico(self):
        return self.correoElectronicoPersonal


class AsignacionResponsableTecnicoRT(models.Model):
    
    fechaDesde = models.DateTimeField(null = True, blank=True)
    fechaHasta = models.DateTimeField(null = True, blank=True)
    personal = models.ForeignKey(PersonalCientifico, on_delete = models.PROTECT, null = True, related_name='personal')
    recursos = models.ForeignKey('recurso.RecursoTecnologico', on_delete = models.PROTECT, null = True, related_name='recurso_tecnologico')

   
    class Meta:
        verbose_name_plural = "AsignacionResponsableTecnicoRT"

    def __str__(self):
        return '{} - {}'.format(self.personal.nombre, self.fechaDesde)

    def crear():
        pass
    def mostrarPersonalCientifico():
        pass
    def inhabilitarUsuario():
        pass
    def habilitarUsuario():
        pass
    def tengoUsuarioHabilitado():
        pass
    def mostrarMisNovedades():
        pass
    def getNombre(self):
        return self.nombre
    def esPersonalCientificoLogueado(self,id_personal):
        return self.get_personal_cientifico() == id_personal

    def buscarRTDisponible(self):
        recursos_disponibles = []
        recursos_del_personal_asignado = self.recursos.all() #Obtengo las instancias de mis recursos
        for recurso in recursos_del_personal_asignado:
            if recurso.esRTDisponible():
                recursos_disponibles.append(recurso)
        return recursos_disponibles

    def getCientificoAsignado(self):
        return self.personal.getNombre()


