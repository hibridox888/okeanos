from django.contrib import admin

# Register your models here.
from .models import Contacto


class ContactoAdmin(admin.ModelAdmin):
    model = Contacto
    search_fields = ['nombre', 'email', 'mensaje']
    list_filter = ['fecha', ]
    readonly_fields = ['fecha', ]
    ordering = ['fecha']


admin.site.register(Contacto, ContactoAdmin)
