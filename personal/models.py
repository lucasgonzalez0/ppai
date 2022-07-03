from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class AsignacionResponsableTecnicoRT(models.Model):
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
