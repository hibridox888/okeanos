# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.template.defaultfilters import truncatechars  # or truncatewords

from ckeditor.fields import RichTextField
from easy_thumbnails.fields import ThumbnailerImageField

CONTENIDO_CHOICES = [
    ('N', "Noticias"),
    ('A', "Actividades"),
    ('P', "Proyecto"),
    ('B', "Blog"),
    ('O', "Otros"),
]


class Post(models.Model):
    sitio = models.URLField(null=True, blank=True)
    creacion = models.DateTimeField(null=True)
    modificacion = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey('auth.User')

    titulo = models.CharField(max_length=400)
    subtitulo = models.CharField(max_length=400, blank=True, null=True)
    ubicacion = models.CharField(max_length=30, blank=True, null=True)
    slug = models.SlugField(unique=True, help_text='Generado a partir del titulo para generar URL')
    tipo = models.CharField(max_length=1, choices=CONTENIDO_CHOICES, default='P')
    resumen = models.TextField()
    descripcion = RichTextField(blank=True, null=True)

    @property
    def _resumen(self):
        return truncatechars(self.resumen, 150)

    def primera_imagen(self):
        return self.imagen_post.first()

    def __unicode__(self):
        return '%s, %s' % (self.titulo, self.autor)

    """
    def get_autor(self):
        if self.autor.first_name is None:
            return 'ProAus'
        else:
            return '%s' % self.autor.first_name
    """

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'


class Archivo(models.Model):
    post = models.ForeignKey(Post, related_name='archivo_post')
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='post/file')

    def __unicode__(self):
        if self.nombre is None:
            return '%s' % self.post.titulo
        elif self.nombre is not None:
            return '%s' % self.nombre

    class Meta:
        verbose_name = 'Archivo'
        verbose_name_plural = 'Archivos'


class Imagen(models.Model):
    post = models.ForeignKey(Post, related_name='imagen_post')
    nombre = models.CharField(max_length=100)
    archivo = ThumbnailerImageField(upload_to='post/img')

    def __unicode__(self):
        if self.nombre is None:
            return '%s' % self.post.titulo
        elif self.nombre is not None:
            return '%s' % self.nombre

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'


class Video(models.Model):
    post = models.ForeignKey(Post, related_name='video_post')
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='post/vid')

    def __unicode__(self):
        if self.nombre is None:
            return '%s' % self.post.titulo
        elif self.nombre is not None:
            return '%s' % self.nombre

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
