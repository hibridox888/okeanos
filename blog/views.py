from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from blog.models import Entry, Tag
from okeanos.views import Pagina


def home(request):
    Pagina.titulo = 'Blog'
    Pagina.subtitulo = 'Subtitulo'
    last_entries = Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now)[:30]
    all_tags = Tag.objects.all()
    return render(request, 'blog/list.html', {
        'pagina': Pagina,
        'last_entries': last_entries,
        'all_tags': all_tags,
    })


def view_author(request, author):
    Pagina.titulo = 'Blog'
    Pagina.subtitulo = 'Subtitulo'
    last_entries = Entry.objects \
                       .filter(is_active=True) \
                       .filter(pub_date__lte=Pagina.now) \
                       .filter(author=author)[:30]
    all_tags = Tag.objects.all()
    return render(request, 'blog/list.html', {
        'pagina': Pagina,
        'last_entries': last_entries,
        'all_tags': all_tags,
    })


def detail_entry(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    all_tags = Tag.objects.all()
    last_entries = Entry.objects.filter(is_active=True).filter(pub_date__lte=Pagina.now)[:30]
    Pagina.titulo = '%s' % entry.headline
    Pagina.subtitulo = '%s' % entry.subheadline
    return render(request, 'blog/detail.html', {
        'pagina': Pagina,
        'entry': entry,
        'all_tags': all_tags,
        'last_entries': last_entries,
    })
