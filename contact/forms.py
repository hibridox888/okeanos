from django import forms

from .models import Contacto


class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=50, label='Nombre', min_length=4)
    email = forms.EmailField(widget=forms.EmailInput(), min_length=4)
    mensaje = forms.CharField(widget=forms.Textarea(
        attrs={'cols': '5', 'rows': '10', 'class': 'materialize-textarea'},
    ), min_length=10)

    class Meta:
        model = Contacto
        fields = ('nombre', 'email', 'mensaje')
