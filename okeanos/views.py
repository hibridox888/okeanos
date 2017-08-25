# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from blog.models import Post, now


class Pagina(object):
    titulo = 'Modelo'
    subtitulo = 'Acción'
    now = now


def home(request):
    last_post = Post.objects.all().order_by('creacion')
    return render(request, 'web/home.html', {
        'pagina': Pagina,
    })
