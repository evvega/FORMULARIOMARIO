from django import forms
from aplicaciones.clientt.models import Client, AddInformation


class CLIENTFORM(forms.ModelForm):

    class Meta:
        model= Client
        fields = [
            'NAME',
            'SURNAMES',
            'AGE',
            'TYPE_GENDER',
            'EMAIL',
            'PHONE',
            'TYPE_CITY',
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
            'TYPE_CITY':'Ciudad',
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
            'TYPE_CITY': forms.Select(attrs={'class': ' form-control'}),
            'SOCIOECONOMIC_LEVEL': forms.TextInput(attrs={'class': ' form-control'}),
            'TICKET': forms.TextInput(attrs={'class': ' form-control'}),
        }

class ADDINFORMATIONFORM(forms.ModelForm):
    class Meta:
        model =AddInformation
        fields = [
            'TYPE_WAYTOPAY',
            'TYPE_PRODUCTQUALIFICATION',
            'TYPE_SERVICEQUALIFICATION',
        ]

        labels ={
            'TYPE_WAYTOPAY':'Forma de pago',
            'TYPE_PRODUCTQUALIFICATION':'Calificacion a nuestro producto',
            'TYPE_SERVICEQUALIFICATION':'Calificacion a nuestro servicio',
        }

        widgets = {
            'TYPE_WAYTOPAY':forms.Select(attrs={'class':'form-control'}),
            'TYPE_PRODUCTQUALIFICATION':forms.Select(attrs={'class':'form-control'}),
            'TYPE_SERVICEQUALIFICATION':forms.Select(attrs={'class':'form-control'}),
        }



