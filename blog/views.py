from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Entry, Tag
from okeanos.views import Pagina


def home(request):
    Pagina.titulo = 'Blog'
    Pagina.subtitulo = 'Subtitulo'
    last_entries = Entry.objects.all()
    all_tags = Tag.objects.all()
    return render(request, 'blog/list.html', {
        'pagina': Pagina,
        'last_entries': last_entries,
        'all_tags': all_tags,
    })
