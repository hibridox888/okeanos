# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import http

from django.shortcuts import render

from blog.models import Entry, now, Tag
from contact.views import form_contact

all_tags = Tag.objects.all()


class Pagina(object):
    titulo = 'Modelo'
    subtitulo = 'Acción'
    description = 'descripción'
    now = now


def home(request):
    Pagina.titulo = 'Modelo'
    Pagina.subtitulo = 'Acción'
    last_entries = Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now)[:30]
    return render(request, 'web/home.html', {
        'pagina': Pagina,
        'last_entries': last_entries,
        'all_tags': all_tags,
        'contact': form_contact(request=request),
    })
