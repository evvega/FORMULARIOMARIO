from django import forms
from aplicaciones.cliente.models import CLIENTCREATE

class CLIENTFORM(forms.ModelForm):

    class Meta:
        model= CLIENTCREATE
        fields = [
            'NAME',
            'SURNAMES',
            'EDAD',
            'TYPE_GENDER',

        ]

        labels= {
            'NAME': 'Nombre',
            'SURNAMES':'Apellidos',
            'EDAD':'Edad',
            'TYPE_GENDER':'Genero',

        }

        widgets = {
            'NAME':forms.TextInput(attrs={'class':' form-control'}),
            'SURNAMES': forms.TextInput(attrs={'class': ' form-control'}),
            'EDAD': forms.TextInput(attrs={'class': ' form-control'}),
            'TYPE_GENDER': forms.RadioSelect }
