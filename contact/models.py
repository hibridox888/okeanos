# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _, ugettext_lazy


# Create your models here.

class Contact(models.Model):
    date = models.DateTimeField(_('date'), auto_now=True, blank=True, null=True, unique=True)
    name = models.CharField(_('name'), max_length=50)
    mail = models.EmailField(_('mail'), )
    message = models.TextField(_('message'), help_text='mensaje del cliente', unique=True)

    def __unicode__(self):
        return u"%s" % (self.name)

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
        ordering = ['name']
