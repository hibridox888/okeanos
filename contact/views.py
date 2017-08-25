# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives
import datetime; now = str(datetime.datetime.now())
from contacto.forms import ContactoForm

def form_contact(request):
    if request.method == "POST":
        contact = ContactoForm(request.POST)
        mensaje_enviado = '/enviando_mensaje/'
        if contact.is_valid():
            c = contact.save(commit=False)
            c.save()
            to_mail = c.email
            subject, from_email, to = 'Copia Mensaje Tipster', 'contacto@tipster.cl', to_mail,
            text_content = 'Gracias por escribirnos'
            html_content = '<h1>Copia del mensaje en Tipster:</h1><br><p><strong>Mensaje: </strong><br>' + c.mensaje + '</p><br><p><strong>De: </strong>' + c.nombre + '(' + c.email + ' - enviado: ' + now + ')</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            print('Enviado a cliente :v')
            to_mail = 'contacto@tipster.cl'
            subject, from_email, to = 'Copia Mensaje Tipster', 'contacto@tipster.cl', to_mail,
            text_content = 'Gracias por escribirnos'
            html_content = '<h1>Copia del mensaje en Tipster:</h1><br><p><strong>Mensaje: </strong><br>' + c.mensaje + '</p><br><p><strong>De: </strong>' + c.nombre + '(' + c.email + ' - enviado: ' + now + ')</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            print('Enviado copia :v')
            return redirect(mensaje_enviado)
    else:
        contact = ContactoForm()
    return contact