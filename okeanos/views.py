# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.shortcuts import render

from blog.models import Entrada, Etiqueta
from contact.views import form_contact


def home(request):
    entradas_proyectos = Entrada.objects.publicado().filter(tipo_publicacion='PR')[:3]
    otras_entradas = Entrada.objects.publicado().exclude(tipo_publicacion='PR')[:3]
    slider_entries = Entrada.objects.publicado().filter(slider=False)[:3]
    last_entries = Entrada.objects.publicado()[:5]
    return render(request, 'web/home.html', {
        'slider_entries': slider_entries,
        'last_entries': last_entries,
        'other_entries': otras_entradas,
        'projects_entries': entradas_proyectos,
        'all_tags': Etiqueta.objects.all(),
        'contact': form_contact(request=request),
    })
