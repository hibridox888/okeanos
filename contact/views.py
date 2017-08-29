# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives

from .forms import ContactoForm
from django.core.urlresolvers import reverse

now = 'Hora: %s:%s Fecha: %s' % (
    datetime.datetime.now().time().hour,
    datetime.datetime.now().time().minute,
    datetime.datetime.now().date())


def form_contact(request):
    if request.method == "POST":
        contact = ContactoForm(request.POST)
        if contact.is_valid():
            c = contact.save(commit=False)
            c.save()
            to_mail = c.email
            subject, from_email, to = 'Copia Mensaje', 'prueba@tucodigo.cl', to_mail,
            text_content = 'Gracias por escribirnos'
            html_content = '<p><strong>Mensaje: </strong><br>' + c.mensaje + '</p><br><p><strong>De: </strong>' + c.nombre + '(' + c.email + ' - enviado: ' + now + ')</p>'
            print(html_content)
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            print('Enviado a cliente :v')
            to_mail = 'contacto@tipster.cl'
            subject, from_email, to = 'Copia Mensaje Tipster', 'prueba@tucodigo.cl', to_mail,
            text_content = 'Gracias por escribirnos'
            html_content = '<p><strong>Mensaje: </strong><br>' + c.mensaje + '</p><br><p><strong>De: </strong>' + c.nombre + '(' + c.email + ' - enviado: ' + now + ')</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            print('Enviado copia :v')
            return redirect('enviado')
    else:
        contact = ContactoForm()
    return contact
