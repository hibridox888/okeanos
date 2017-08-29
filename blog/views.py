# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import Entry, Tag
from contact.views import form_contact
from okeanos.views import Pagina

all_entries = Entry.objects \
                  .filter(is_active=True) \
                  .filter(pub_date__lte=Pagina.now)[:30]

all_tags = Tag.objects.all()

def home(request):
    Pagina.titulo = 'Todas las Entradas'
    Pagina.subtitulo = 'Noticias, '
    last_entries = Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now)[:30]
    return render(request, 'blog/list.html', {
        'pagina': Pagina,
        'last_entries': last_entries,
        'all_tags': all_tags,
        'all_entries': all_entries,
        'contact': form_contact(request=request),
    })


def list_author(request, username):
    Pagina.titulo = 'Post por el autor:'
    Pagina.subtitulo = '%s' % username
    last_entries = Entry.objects \
                       .filter(is_active=True) \
                       .filter(pub_date__lte=Pagina.now) \
                       .filter(author__username=username)[:30]
    return render(request, 'blog/list.html', {
        'pagina': Pagina,
        'last_entries': last_entries,
        'all_tags': all_tags,
        'all_entries': all_entries,
        'contact': form_contact(request=request),
    })


def list_tag(request, title):
    Pagina.description = 'OKEANOS, Tecnología marina'
    Pagina.titulo = 'Etiqueta:'
    Pagina.subtitulo = '%s' % title
    last_entries = Entry.objects \
                       .filter(is_active=True) \
                       .filter(pub_date__lte=Pagina.now) \
                       .filter(tags__title=title)[:30]
    return render(request, 'blog/list.html', {
        'pagina': Pagina,
        'last_entries': last_entries,
        'all_tags': all_tags,
        'all_entries': all_entries,
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
        'all_tags': all_tags,
        'last_entries': last_entries,
        'all_entries': all_entries,
        'contact': form_contact(request=request),
    })
