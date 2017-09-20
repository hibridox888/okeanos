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
    ('N', _("New")),
    ('P', _("Project")),
    ('E', _("Post")),
    ('O', _("Other")),
    ('V', _("Event")),
]


class Tag(models.Model):
    title = models.CharField(_('title'), max_length=30)

    def __unicode__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = _('tags')
        verbose_name = _('tag')


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
        verbose_name=_("pub date"),
        help_text="Para que una publicación sea publicada, debe estar activa y su fecha de publicación debe estar en el pasado",
        default=now,
    )
    author = models.ForeignKey('auth.User', verbose_name=_('author'))
    slug = models.SlugField(_('slug'), unique_for_date='pub_date')
    publication_type = models.CharField(_('publication type'), max_length=1, choices=CONTENT_CHOICES, default='E')

    # if redirect to other site
    external_url = models.URLField(_("external url"), null=True, blank=True,
                                   help_text="Si se deja vacío este campo, los links para ver más detalles redireccionarán dentro del sitio al detalle. "
                                             "Al ingresar una URL en este campo se redireccionará a este cuando se pidan detalles ")

    # define content
    headline = models.CharField(_('headline'), max_length=200)
    subheadline = models.CharField(_('subheadline'), max_length=200, blank=True, null=True)
    location = models.CharField(_('location'), max_length=40, blank=True, null=True)
    summary = models.CharField(_('summary'), max_length=300, blank=True, null=True)
    content = RichTextField(_('content'), blank=True, null=True)

    objects = EntryQuerySet.as_manager()

    is_active = models.BooleanField(
        _('if is active'),
        help_text=
        "Marque para hacer esta entrada en vivo (ver también la fecha de publicación). "
        "Tenga en cuenta que los administradores (como usted) tienen permiso para previsualizar "
        "Entradas inactivas mientras que el público en general no"
        ,
        default=False,
    )

    # Others
    tags = models.ManyToManyField(Tag,
                                  verbose_name=_('tag'),
                                  related_name='entry_tag',
                                  blank=True)
    on_slider = models.BooleanField(
        _('active in slider'),
        help_text=
            "Marque para que sea visible en el slider "
            "Se visualizará primero el inicial y luego los que sean visibles en slider "
            "Pueden marcar hasta 6 para ser visibles, es necesaria una imagen, de no ser subida una imágen no se mostrará "
        ,
        default=False,
    )
    facebook_comments = models.BooleanField(
        _('to enable facebook comments'),
        help_text=
            "Marque para que sea visible el plugin de facebook para realizar comentarios "
            "No se tendrá mayor control sobre los comentarios "
        ,
        default=False,
    )

    def get_admin_url(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return urlresolvers.reverse("admin:%s_%s_change" % (content_type.app_label, content_type.model),
                                    args=(self.id,))

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
        verbose_name = _('entry')
        verbose_name_plural = _('entries')


class File(models.Model):
    entry = models.ForeignKey(Entry, verbose_name=_('entry'),related_name='file_entry')
    name = models.CharField(_('name'), max_length=100, blank=True, null=True)
    file = models.FileField(_('file location'), upload_to='entries/file')

    def __unicode__(self):
        if self.name:
            return '%s' % self.name
        else:
            return basename(self.file.name)

    class Meta:
        verbose_name = _('file')
        verbose_name_plural = _('files')


class Image(models.Model):
    entry = models.ForeignKey(Entry, related_name='image_post')
    name = models.CharField(_('name'), max_length=100, blank=True, null=True)
    file = ThumbnailerImageField(_('file location'), upload_to='entries/img')

    def __unicode__(self):
        if self.name:
            return '%s' % self.name
        else:
            return basename(self.file.name)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')


class Video(models.Model):
    entry = models.ForeignKey(Entry, related_name='video_post')
    name = models.CharField(_('name'), max_length=100, blank=True, null=True)
    file = models.FileField(_('file location'), upload_to='entries/vid')

    def __unicode__(self):
        if self.name:
            return '%s' % self.name
        else:
            return basename(self.file.name)

    class Meta:
        verbose_name = _('video')
        verbose_name_plural = _('videos')
