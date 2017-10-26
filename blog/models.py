# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from os.path import basename

# Create your models here.
from django.db import models
from django.template.defaultfilters import truncatechars  # or truncatewords
from django.utils.translation import ugettext as _, ugettext_lazy
from django_hosts.resolvers import reverse
from ckeditor.fields import RichTextField
from easy_thumbnails.fields import ThumbnailerImageField
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType

now = datetime.datetime.now()

CONTENT_CHOICES = [
    ('NU', _("Nuevo")),
    ('PR', _("Proyecto")),
    ('PO', _("Posteo")),
    ('OT', _("Otro")),
    ('EV', _("Evento")),
]


class Etiqueta(models.Model):
    titulo = models.CharField(_('titulo'), max_length=30)

    def __unicode__(self):
        return '%s' % self.titulo

    class Meta:
        ordering = ('titulo',)
        verbose_name = _('etiqueta')
        verbose_name_plural = _('etiquetas')


class EntradaQuerySet(models.QuerySet):
    def publicado(self):
        return self.activo().filter(fecha_publicacion__lte=datetime.datetime.now())

    def activo(self):
        return self.filter(visible=True)


class Entrada(models.Model):
    # metadata
    creacion = models.DateTimeField(_('creación'), null=True, auto_created=True, editable=False)
    modificacion = models.DateTimeField(_('modificación'), auto_now=True, editable=False)
    fecha_publicacion = models.DateTimeField(
        verbose_name=_("fecha de publicación"), default=datetime.datetime.now,
        help_text="Para que una publicación sea publicada, debe estar activa y su fecha de publicación debe estar en el pasado", )
    autor = models.ForeignKey(
        'auth.User',
        verbose_name=_('autor'), )
    slug = models.SlugField(
        _('slug'),
        unique_for_date='fecha_publicacion',
        help_text='Debe ser unica en el mes y sirve para generar la url asociada, se genera automaticamente', )
    # if redirect to other site
    url_externa = models.URLField(
        _("url externa"), null=True, blank=True,
        help_text="Si se deja vacío este campo, los links para ver más detalles redireccionarán dentro del sitio al detalle. "
                  "Al ingresar una URL en este campo se redireccionará a este cuando se pidan detalles ")
    # content in publication
    tipo_publicacion = models.CharField(
        _('tipo de publicación'), max_length=2, choices=CONTENT_CHOICES, default='PO',
        help_text='Puede ser cualquier cosa: Eventos, posteos, proyectos, etc..')
    titulo = models.CharField(_('titulo'), max_length=200, help_text='Titulo de la publicación', )
    subtitulo = models.CharField(_('subtitulo'), max_length=200, blank=True, null=True,
                                 help_text='Subtitulo de la publicación', )
    ubicacion = models.CharField(_('ubicación'), max_length=40, blank=True, null=True)
    resumen = models.CharField(_('resumen'), max_length=300, blank=True, null=True)
    contenido = RichTextField(_('contenido'), blank=True, null=True)

    objects = EntradaQuerySet.as_manager()

    visible = models.BooleanField(
        _('se encuentra visible'),
        help_text=
        "Marque para hacer esta entrada en vivo (ver también la fecha de publicación). "
        "Tenga en cuenta que los administradores (como usted) tienen permiso para previsualizar "
        "Entradas inactivas mientras que el público en general no",
        default=False,
    )

    # Options
    etiqueta = models.ManyToManyField(Etiqueta,
                                      verbose_name=_('etiqueta'),
                                      related_name='entry_tag',
                                      blank=True)
    slider = models.BooleanField(
        _('activo en el slider'), default=False,
        help_text=
        "Marque para que sea visible en el slider "
        "Se visualizará primero el inicial y luego los que sean visibles en slider "
        "Pueden marcar hasta 6 para ser visibles, es necesaria una imagen, de no ser subida una imágen no se mostrará ",
    )
    comentarios_facebook = models.BooleanField(
        _('comentarios de Facebook'),
        help_text=
        "Marque para que sea visible el plugin de facebook para realizar comentarios "
        "No se tendrá mayor control sobre los comentarios ",
        default=False,
    )

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model),
                                    args=(self.id,))

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blogweb_blog:detail_entry', args=[str(self.slug)])

    def es_publicado(self):
        """
        Return True if the entry is publicly accessible.
        """
        return self.visible and self.fecha_publicacion <= datetime.datetime.now()

    es_publicado.boolean = True

    def publicado(self):
        return self.objects.activo().filter(fecha_publicacion__lte=datetime.datetime.now)

    @property
    def _resumen(self):
        return truncatechars(self.resumen, 150)

    def primera_imagen(self):
        return self.imagen_entrada.first()

    def __unicode__(self):
        return '%s, %s' % (self.titulo, self.autor)

    class Meta:
        ordering = ('-fecha_publicacion',)
        get_latest_by = 'fecha_publicacion'
        verbose_name = _('entrada')
        verbose_name_plural = _('entradas')


class Documento(models.Model):
    entrada = models.ForeignKey(Entrada, verbose_name=_('entrada'), related_name='documento_entrada')
    nombre = models.CharField(_('nombre'), max_length=100, blank=True, null=True)
    archivo = models.FileField(_('archivo'), upload_to='uploads/D/%Y/%m/%d/')

    def __unicode__(self):
        if self.nombre:
            return '%s' % self.nombre
        else:
            return basename(self.archivo.name)

    class Meta:
        verbose_name = _('documento')
        verbose_name_plural = _('documentos')


class Imagen(models.Model):
    entrada = models.ForeignKey(Entrada, verbose_name=_('entrada'), related_name='imagen_entrada')
    nombre = models.CharField(_('nombre'), max_length=100, blank=True, null=True,
                              help_text='ej: Horario, tickets, presentación, etc')
    archivo = models.FileField(_('archivo'), upload_to='uploads/I/%Y/%m/%d/')

    def __unicode__(self):
        if self.nombre:
            return '%s' % self.nombre
        else:
            return basename(self.archivo.name)

    class Meta:
        verbose_name = _('imagen')
        verbose_name_plural = _('imagenes')


class Video(models.Model):
    entrada = models.ForeignKey(Entrada, verbose_name=_('entrada'), related_name='video_entrada')
    nombre = models.CharField(_('nombre'), max_length=100, blank=True, null=True)
    archivo = models.FileField(_('archivo'), upload_to='uploads/V/%Y/%m/%d/')

    def __unicode__(self):
        if self.nombre:
            return '%s' % self.nombre
        else:
            return basename(self.archivo.name)

    class Meta:
        verbose_name = _('video')
        verbose_name_plural = _('videos')
