# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import http

from django.shortcuts import render, render_to_response
from django.template import RequestContext, TemplateDoesNotExist
from django.template import Context, Engine, TemplateDoesNotExist, loader
from django.views.decorators.csrf import requires_csrf_token
from django.views.defaults import ERROR_400_TEMPLATE_NAME

from blog.models import Entry, now


class Pagina(object):
    titulo = 'Modelo'
    subtitulo = 'Acción'
    now = now


def home(request):
    last_entries = Entry.objects.all().order_by('creacion')
    return render(request, 'web/home.html', {
        'pagina': Pagina,
        'last_entries': last_entries,
    })

