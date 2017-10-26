# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Etiqueta, Entrada, Imagen, Documento, Video


class EtiquetaInLine(admin.TabularInline):
    model = Etiqueta


# Register your models here.
class ImagenInline(admin.TabularInline):
    model = Imagen
    fields = ['nombre', 'archivo']
    extra = 1
    max_num = 9


class VideoInline(admin.TabularInline):
    model = Video
    fields = ['nombre', 'archivo']
    extra = 0
    max_num = 3


class DocumentoInline(admin.TabularInline):
    model = Documento
    fields = ['nombre', 'archivo']
    extra = 0
    max_num = 9


class EntradaAdmin(admin.ModelAdmin):
    model = Entrada
    search_fields = ['titulo', 'resumen', ]
    readonly_fields = ['creacion', 'modificacion', ]
    list_display = ['titulo', 'autor', 'tipo_publicacion', 'resumen']
    inlines = [ImagenInline, DocumentoInline, VideoInline]
    list_filter = ['visible', 'fecha_publicacion', 'autor', 'tipo_publicacion', 'ubicacion']
    prepopulated_fields = {
        'slug': ('titulo',),
    }
    fieldsets = (
        ('General', {
            'fields': (('etiqueta', 'tipo_publicacion'),
                       ('slider', 'comentarios_facebook'), 'url_externa'),
            # 'classes': ('collapse',)
        }),
        ('Contenido', {
            'fields': (('titulo', 'ubicacion',), 'visible', 'subtitulo', 'resumen', 'contenido',),
            # 'classes': ('collapse',)
        }),
        ('Adicionales', {
            'fields': ('fecha_publicacion', 'slug',),
            'classes': ('collapse',)
        }),
    )
    ordering = ['fecha_publicacion', ]

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        obj.save()


admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Etiqueta)
