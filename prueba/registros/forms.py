from django import forms
from .models import ComentarioContacto

class ComtarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario', 'mensaje']