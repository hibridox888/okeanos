from __future__ import unicode_literals
from django import forms
from django.utils.translation import ugettext as _, ugettext_lazy

from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50, label=_('name'))
    mail = forms.EmailField(widget=forms.EmailInput(), min_length=4)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'cols': '5', 'rows': '10', 'class': 'materialize-textarea'},
    ), min_length=10)

    class Meta:
        model = Contact
        fields = ('name', 'mail', 'message')
