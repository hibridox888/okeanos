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


# HTTP Error 400

@requires_csrf_token
def bad_request(request, exception, template_name='404.html'):
    """
    400 error handler.

    Templates: :template:`400.html`
    Context: None
    """
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        if template_name != ERROR_400_TEMPLATE_NAME:
            # Reraise if it's a missing custom template.
            raise
        return http.HttpResponseBadRequest('<h1>Bad Request (400)</h1>', content_type='text/html')
    # No exception content is passed to the template, to not disclose any sensitive information.
    return http.HttpResponseBadRequest(template.render())
