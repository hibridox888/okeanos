# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import Entry, Tag
from contact.views import form_contact
from okeanos.views import Pagina
from django.utils.translation import ugettext as _, ugettext_lazy


def home(request):
    Pagina.titulo = _('Todas las Entradas')
    Pagina.subtitulo = _('Noticias, proyectos, post y eventos')
    last_entries = Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now)[:30]
    return render(request, 'blog/list.html', {
        'pagina': Pagina,
        'last_entries': last_entries,
        'Tag.objects.all()': Tag.objects.all(),
        'all_entries': Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now)[:30],
        'contact': form_contact(request=request),
    })


def list_author(request, username):
    Pagina.titulo = _('Post por el autor:')
    Pagina.subtitulo = '%s' % username
    last_entries = Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now).filter(
        author__username=username)[:30]
    return render(request, 'blog/list.html', {
        'pagina': Pagina,
        'last_entries': last_entries,
        'Tag.objects.all()': Tag.objects.all(),
        'all_entries': Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now)[:30],
        'contact': form_contact(request=request),
    })


def list_tag(request, title):
    Pagina.description = _('OKEANOS, Tecnología marina')
    Pagina.titulo = _('Etiqueta:')
    Pagina.subtitulo = '%s' % title
    last_entries = Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now).filter(tags__title=title)[:30]
    return render(request, 'blog/list.html', {
        'pagina': Pagina,
        'last_entries': last_entries,
        'Tag.objects.all()': Tag.objects.all(),
        'all_entries': Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now)[:30],
        'contact': form_contact(request=request),
    })


def detail_entry(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    last_entries = Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now)[:30]
    Pagina.titulo = '%s' % entry.headline
    Pagina.subtitulo = '%s' % entry.subheadline
    Pagina.description = '%s' % entry.summary
    return render(request, 'blog/detail.html', {
        'pagina': Pagina,
        'entry': entry,
        'Tag.objects.all()': Tag.objects.all(),
        'last_entries': last_entries,
        'all_entries': Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now)[:30],
        'contact': form_contact(request=request),
    })
