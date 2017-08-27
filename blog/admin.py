# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from modeltranslation.translator import translator, TranslationOptions

from django.contrib import admin
from .models import Entry, Image, File, Video, Tag


class TagInLine(admin.TabularInline):
    model = Tag


# Register your models here.
class ImageEntryInline(admin.TabularInline):
    model = Image
    fields = ['name', 'file']
    extra = 1
    max_num = 9


class VideoEntryInline(admin.TabularInline):
    model = Video
    fields = ['name', 'file']
    extra = 0
    max_num = 3


class FileEntryInline(admin.TabularInline):
    model = File
    fields = ['name', 'file']
    extra = 0
    max_num = 9


class EntryAdmin(admin.ModelAdmin):
    model = Entry
    search_fields = ['headline', 'summary', ]
    readonly_fields = ['created', 'modify', ]
    list_display = ['headline', 'author', 'publication_type', 'resumen']
    inlines = [ImageEntryInline, FileEntryInline, VideoEntryInline]
    list_filter = ['is_active', 'pub_date', 'author', 'publication_type', 'location']
    prepopulated_fields = {
        'slug': ('headline',),
    }
    fieldsets = (
        ('General', {
            'fields': (('tags','publication_type'), 'on_slider', 'external_url'),
            # 'classes': ('collapse',)
        }),
        ('Contenido', {
            'fields': ('is_active', 'headline', 'subheadline', 'location', 'summary', 'content',),
            # 'classes': ('collapse',)
        }),
        ('Adicionales', {
            'fields': ('pub_date', 'slug',),
            'classes': ('collapse',)
        }),
    )
    ordering = ['pub_date', ]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)
