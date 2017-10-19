from django import forms
from aplicaciones.cliente.models import CLIENT


class CLIENTFORM(forms.ModelForm):

    class Meta:
        model= CLIENT
        fields = [
            'NAME',
            'SURNAMES',
            'AGE',
            'TYPE_GENDER',
            'EMAIL',
            'PHONE',
            'CITY',
            'SOCIOECONOMIC_LEVEL',
            'TICKET',

        ]

        labels = {
            'NAME': 'Nombre',
            'SURNAMES':'Apellidos',
            'AGE': 'Edad',
            'TYPE_GENDER':'Genero',
            'EMAIL':'Email',
            'PHONE':'Telefono',
            'CITY':'Ciudad',
            'SOCIOECONOMIC_LEVEL':'Nivel socioeconomico',
            'TICKET':'Ticket',

        }

        widgets = {
            'NAME':forms.TextInput(attrs={'class':' form-control'}),
            'SURNAMES': forms.TextInput(attrs={'class': ' form-control'}),
            'AGE': forms.TextInput(attrs={'class': ' form-control'}),
            'TYPE_GENDER': forms.Select(attrs={'class': ' form-control'}),
            'EMAIL': forms.TextInput(attrs={'class':'form-control'}),
            'PHONE': forms.TextInput(attrs={'class':'form-control'}),
            'CITY': forms.TextInput(attrs={'class': ' form-control'}),
            'SOCIOECONOMIC_LEVEL': forms.TextInput(attrs={'class': ' form-control'}),
            'TICKET': forms.TextInput(attrs={'class': ' form-control'}),
        }
