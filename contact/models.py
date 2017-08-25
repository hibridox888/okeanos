# coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Contacto(models.Model):
    fecha = models.DateTimeField(auto_now=True, blank=True, null=True)
    nombre = models.CharField('Nombre o Empresa', max_length=50)
    email = models.EmailField('Email')
    mensaje = models.TextField(help_text='Un mensaje')

    def __unicode__(self):
        return u"%s" % (self.nombre)

    class Meta:
        verbose_name = "Persona o Empresa"
        verbose_name_plural = "Personas o Empresas"
        ordering = ['nombre']
