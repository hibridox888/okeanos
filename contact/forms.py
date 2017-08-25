from django import forms

from .models import Contacto


class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(label='nombre', max_length=30,
                             widget=forms.TextInput(attrs={'placeholder': 'Escribe tu nombre'}))
    email = forms.EmailField(label='email',
                             widget=forms.EmailInput(attrs={'placeholder': 'Escribe tu email'}))
    mensaje = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Escribe tu mensaje',
               'cols': '10', 'rows': '10',
               'class': 'materialize-textarea'},
    ))

    class Meta:
        model = Contacto
        fields = ('nombre', 'email', 'mensaje')
