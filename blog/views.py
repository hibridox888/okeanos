# coding=utf-8

import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Entrada, Etiqueta
from contact.views import form_contact
from django.utils.translation import ugettext as _


def home(request):
    ultimas_entradas = Entrada.objects.publicado()[:30]
    return render(request, 'blog/list.html', {
        'titulo': 'Todas las Entradas',
        'subtitulo': 'Noticias, proyectos, post y eventos',
        'descripcion': 'Descripción',
        'last_entries': ultimas_entradas,
        'Tag.objects.all()': Etiqueta.objects.all(),
        'all_entries': Entrada.objects.publicado()[:30],
        'contact': form_contact(request=request),
    })


def list_author(request, username):
    last_entries = Entrada.objects.publicado().filter(
        autor__username=username)[:30]
    return render(request, 'blog/list.html', {
        'pagina': 'Post por el autor:' % username,
        'last_entries': last_entries,
        'Tag.objects.all()': Entrada.objects.all(),
        'all_entries': Entrada.objects.publicado()[:30],
        'contact': form_contact(request=request),
    })


def list_tag(request, title):
    ultimas_entradas = Entrada.objects.publicado()[:30]
    return render(request, 'blog/list.html', {
        'last_entries': ultimas_entradas,
        'Tag.objects.all()': Entrada.objects.all(),
        'all_entries': Entrada.objects.publicado()[:30],
        'contact': form_contact(request=request),
    })


def detail_entry(request, slug):
    entrada = get_object_or_404(Entrada, slug=slug)
    last_entries = Entrada.objects.publicado()[:30]
    return render(request, 'blog/detail.html', {
        'entrada': entrada,
        'last_entries': last_entries,
        'all_tags': Etiqueta.objects.all(),
        'all_entries': Entrada.objects.publicado()[:30],
        'contact': form_contact(request=request),
    })
