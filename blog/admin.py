# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post, Archivo, Imagen, Video


# Register your models here.
class VideoPostInline(admin.TabularInline):
    model = Video
    fields = ['nombre', 'archivo']
    extra = 0


class ImagenPostInline(admin.TabularInline):
    model = Imagen
    fields = ['nombre', 'archivo']
    extra = 1


class ArchivoPostInline(admin.TabularInline):
    model = Archivo
    fields = ['nombre', 'archivo']
    extra = 0


class PostAdmin(admin.ModelAdmin):
    model = Post
    search_fields = ['titulo', 'resumen']
    readonly_fields = ['modificacion', ]
    list_display = ['titulo', 'autor', 'tipo', '_resumen']
    inlines = [ImagenPostInline, ArchivoPostInline, VideoPostInline]
    list_filter = ['creacion', 'autor', 'tipo', 'ubicacion']
    prepopulated_fields = {
        'slug': ('titulo',),
    }
    fieldsets = ((
                     'MetaDatos', {
                         'fields': (('creacion', 'modificacion'), 'slug'),
                         'classes': ('collapse',)
                     }), (
                     'General', {
                         'fields': (('sitio'), 'autor',
                                    'titulo', 'subtitulo',
                                    ('tipo', 'ubicacion')),
                         # 'classes': ('collapse',)
                     }), (
                     'Contenido', {
                         'fields': ('resumen', 'descripcion'),
                         # 'classes': ('collapse',)
                     })
    )
    ordering = ['creacion']
    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
