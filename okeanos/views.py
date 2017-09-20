# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import http

from django.shortcuts import render

from blog.models import Entry, now, Tag
from contact.views import form_contact

class Pagina(object):
    titulo = 'Modelo'
    subtitulo = 'Acción'
    description = 'descripción'
    now = now


def home(request):
    Pagina.titulo = 'Okeanos Marine Technology'
    Pagina.subtitulo = 'Home'
    Pagina.description = 'Nos dedicamos a desarrollar tecnologías de punta en robótica, monitoreo remoto y control a distancia dentro de entornos marinos. Trabajamos desde los 39 grados de latitud sur para proveer soluciones y soporte a clientes de todo el mundo.'
    projects_entries = Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now).filter(publication_type='P')[:3]
    other_entries = Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now).exclude(publication_type='P')[:3]
    last_entries = Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now)[:3]
    return render(request, 'web/home.html', {
        'pagina': Pagina,
        'last_entries': last_entries,
        'other_entries': other_entries,
        'projects_entries': projects_entries,
        'all_tags': Tag.objects.all(),
        'contact': form_contact(request=request),
    })
