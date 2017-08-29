# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

# Create your models here.
from django.db import models
from django.template.defaultfilters import truncatechars  # or truncatewords
from django.utils.translation import ugettext as _, ugettext_lazy
from django_hosts.resolvers import reverse
from ckeditor.fields import RichTextField
from easy_thumbnails.fields import ThumbnailerImageField

now = datetime.datetime.now()

CONTENT_CHOICES = [
    ('N', _("Noticias")),
    ('P', _("Proyectos")),
    ('E', _("Entradas")),
    ('O', _("Otros")),
    ('V', _("Eventos")),
]


class Tag(models.Model):
    title = models.CharField(max_length=30)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = _('etiquetas')
        verbose_name = _('etiqueta')


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.active().filter(pub_date__lte=now)

    def active(self):
        return self.filter(is_active=True)


class Entry(models.Model):
    # metadata
    created = models.DateTimeField(_('creado'), null=True, auto_created=True, editable=False)
    modify = models.DateTimeField(_('modificado'), auto_now=True, editable=False)
    pub_date = models.DateTimeField(
        verbose_name=_("fecha publicación"),
        help_text=_(
            "For an entry to be published, it must be active and its "
            "publication date must be in the past."
        ),
        default=now,
    )
    author = models.ForeignKey('auth.User', verbose_name=_('autor'))
    slug = models.SlugField(_('slug'), unique_for_date='pub_date')
    publication_type = models.CharField(_('tipo de publicación'), max_length=1, choices=CONTENT_CHOICES, default='E')

    # if redirect to other site
    external_url = models.URLField(_("url externa"), null=True, blank=True)

    # define content
    headline = models.CharField(_('titulo'), max_length=200)
    subheadline = models.CharField(_('subtitulo'), max_length=200, blank=True, null=True)
    location = models.CharField(_('lugar'), max_length=40, blank=True, null=True)
    summary = models.CharField(_('resumen'), max_length=300, blank=True, null=True)
    content = RichTextField(_('contenido'), blank=True, null=True)

    objects = EntryQuerySet.as_manager()

    is_active = models.BooleanField(
        _('se encuentra activo'),
        help_text=_(
            "Marque para hacer esta entrada en vivo (ver también la fecha de publicación) "
            "Tenga en cuenta que los administradores (como usted) tienen permiso para previsualizar  "
            "Entradas inactivas mientras que el público en general no lo son "
        ),
        default=False,
    )

    # Others
    tags = models.ManyToManyField(Tag, verbose_name=_('etiqueta'), related_name='entry_tag',
                                  blank=True)
    on_slider = models.BooleanField(
        _('visible en slider'),
        help_text=_(
            "Marque para que sea visible en el slider "
            "Se visualizará primero el inicial y luego los que sean visibles en slider "
            "Pueden marcar hasta 6 para ser visibles, es necesaria una imagen, de no ser subida una imágen no se mostrará "
        ),
        default=False,
    )

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('blogweb_blog:detail_entry', args=[str(self.slug)])

    def is_published(self):
        """
        Return True if the entry is publicly accessible.
        """
        return self.is_active and self.pub_date <= now

    is_published.boolean = True

    def published(self):
        return self.active().filter(pub_date__lte=now)

    @property
    def resumen(self):
        return truncatechars(self.summary, 150)

    def first_img(self):
        return self.image_post.first()

    def __unicode__(self):
        return '%s, %s' % (self.headline, self.author)

    class Meta:
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
        verbose_name = _('entrada')
        verbose_name_plural = _('entradas')


class File(models.Model):
    entry = models.ForeignKey(Entry, related_name='file_entry')
    name = models.CharField(_('nombre'), max_length=100, blank=True, null=True)
    file = models.FileField(_('url'), upload_to='entries/file')

    def __unicode__(self):
        if self.name:
            return '%s' % self.name
        else:
            return '%s' % self.file.name

    class Meta:
        verbose_name = _('archivo')
        verbose_name_plural = _('archivos')


class Image(models.Model):
    entry = models.ForeignKey(Entry, related_name='image_post')
    name = models.CharField(_('nombre'), max_length=100, blank=True, null=True)
    file = ThumbnailerImageField(_('url'), upload_to='entries/img')

    def __unicode__(self):
        if self.name:
            return '%s' % self.name
        else:
            return '%s' % self.file.name

    class Meta:
        verbose_name = _('imagen')
        verbose_name_plural = _('imagenes')


class Video(models.Model):
    entry = models.ForeignKey(Entry, related_name='video_post')
    name = models.CharField(_('nombre'), max_length=100, blank=True, null=True)
    file = models.FileField(_('url'), upload_to='entries/vid')

    def __unicode__(self):
        if self.name:
            return '%s' % self.name
        else:
            return '%s' % self.file.name

    class Meta:
        verbose_name = _('video')
        verbose_name_plural = _('videos')
