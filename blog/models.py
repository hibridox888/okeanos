# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

# Create your models here.
from django.db import models
from django.template.defaultfilters import truncatechars  # or truncatewords
from django.utils.translation import ugettext_lazy as _
from django_hosts.resolvers import reverse
from ckeditor.fields import RichTextField
from easy_thumbnails.fields import ThumbnailerImageField

now = datetime.datetime.now()

CONTENT_CHOICES = [
    ('N', _("News")),
    ('P', _("Projects")),
    ('E', _("Entry")),
    ('O', _("Others")),
    ('E', _("Events")),
]


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.active().filter(pub_date__lte=now)

    def active(self):
        return self.filter(is_active=True)


class Entry(models.Model):
    # metadata
    created = models.DateTimeField(_('created'), null=True, auto_created=True, editable=False)
    modify = models.DateTimeField(_('modify'), auto_now=True, editable=False)
    pub_date = models.DateTimeField(
        verbose_name=_("publication date"),
        help_text=_(
            "For an entry to be published, it must be active and its "
            "publication date must be in the past."
        ),
    )
    author = models.ForeignKey('auth.User', )
    slug = models.SlugField(_('slug'), unique_for_date='pub_date')
    publication_type = models.CharField(_('publication type'), max_length=1, choices=CONTENT_CHOICES, default='P')

    # if redirect to other site
    external_url = models.URLField(_('external url'), null=True, blank=True)

    # define content
    headline = models.CharField(_('headline'), max_length=200)
    subtitle = models.CharField(_('subtitle'), max_length=200, blank=True, null=True)
    location = models.CharField(_('location'), max_length=40, blank=True, null=True)
    summary = models.TextField(_('summary'), blank=True, null=True)
    content = RichTextField(_('content'), blank=True, null=True)

    objects = EntryQuerySet.as_manager()

    is_active = models.BooleanField(
        _('is active'),
        help_text=_(
            "Tick to make this entry live (see also the publication date). "
            "Note that administrators (like yourself) are allowed to preview "
            "inactive entries whereas the general public aren't."
        ),
        default=False,
    )

    def get_absolute_url(self):
        kwargs = {
            'year': self.pub_date.year,
            'month': self.pub_date.strftime('%b').lower(),
            'day': self.pub_date.strftime('%d').lower(),
            'slug': self.slug,
        }
        return reverse('weblog:entry', kwargs=kwargs)

    def is_published(self):
        """
        Return True if the entry is publicly accessible.
        """
        return self.is_active and self.pub_date <= now

    is_published.boolean = True

    def published(self):
        return self.active().filter(pub_date__lte=now)

    @property
    def _resumen(self):
        return truncatechars(self.resumen, 150)

    def primera_imagen(self):
        return self.imagen_post.first()

    def __unicode__(self):
        return '%s, %s' % (self.titulo, self.autor)

    class Meta:
        db_table = 'blog_entries'
        ordering = ('-pub_date',)
        get_latest_by = 'pub_date'
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'


class Archivo(models.Model):
    post = models.ForeignKey(Entry, related_name='archivo_post')
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
