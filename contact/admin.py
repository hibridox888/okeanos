from django.contrib import admin

# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    search_fields = ['name', 'mail', 'message']
    list_filter = ['date', ]
    readonly_fields = ['date', ]
    ordering = ['date']


admin.site.register(Contact, ContactAdmin)
