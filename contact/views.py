# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.shortcuts import redirect
from django.core.mail import EmailMultiAlternatives

from contact.models import Contact
from .forms import ContactForm
from django.core.urlresolvers import reverse

now = 'Hora: %s:%s Fecha: %s' % (
    datetime.datetime.now().time().hour,
    datetime.datetime.now().time().minute,
    datetime.datetime.now().date())


def form_contact(request):
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            c = contact.save(commit=False)
            if c.message == Contact.objects.filter(message=c.message):
                contact = ContactForm()
                pass
            elif '<' in c.message:
                print('se intentó con <')
                contact = ContactForm()
                pass
            elif '</' in c.message:
                contact = ContactForm()
                pass
            elif '<img' in c.message:
                contact = ContactForm()
                pass
            elif '<img' in c.message:
                contact = ContactForm()
            elif '==' in c.message:
                contact = ContactForm()
                pass
            else:
                c.save()
                to_mail = c.mail
                subject, from_email, to = 'Copia Mensaje', 'prueba@tucodigo.cl', to_mail,
                text_content = 'Gracias por escribirnos'
                html_content = '<p><strong>Mensaje: </strong><br>' + c.message + '</p><br><p><strong>De: </strong>' + c.name + '(' + c.mail + ' - enviado: ' + now + ')</p>'
                print(html_content)
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                print('Enviado a cliente :v')
                to_mail = 'prueba@tucodigo.cl'
                subject, from_email, to = 'Copia Mensaje Tipster', 'prueba@tucodigo.cl', to_mail,
                text_content = 'Gracias por escribirnos'
                html_content = '<p><strong>Mensaje: </strong><br>' + c.message + '</p><br><p><strong>De: </strong>' + c.name + '(' + c.mail + ' - enviado: ' + now + ')</p>'
                msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()
                print('Enviado copia :v')
                return redirect('enviado')
    else:
        contact = ContactForm()
    return contact
