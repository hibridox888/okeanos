# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

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
