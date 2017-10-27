from django import forms
from aplicaciones.cliententerprise.models import Enterprise, AddInformation


class EnterprisefForm(forms.ModelForm):

    class Meta:
        model= Enterprise
        fields=[
            'BUSSINES_NAME',
            'NIT',
            'PHONE',
            'EMAIL',
            'TYPE_CITY_COMPANY',
            'ADDRESS',
            'TICKET',
        ]

        labels = {
            'BUSSINES_NAME':'Razon social: ',
            'NIT':'Nit:',
            'PHONE':'Telefono:',
            'EMAIL':'Email:',
            'TYPE_CITY_COMPANY':'Ciudad:',
            'ADDRESS':'Direccion:',
            'TICKET':'Ticket:',

        }

        widgets = {
            'BUSSINES_NAME':forms.TextInput(attrs={'class':'form-control'}),
            'NIT':forms.TextInput(attrs={'class':'form-control'}),
            'PHONE':forms.TextInput(attrs={'class':'form-control'}),
            'EMAIL':forms.TextInput(attrs={'class':'form-control'}),
            'TYPE_CITY_COMPANY': forms.Select(attrs={'class':'form-control'}),
            'ADDRESS':forms.TextInput(attrs={'class':'form-control'}),
            'TICKET':forms.TextInput(attrs={'class':'form-control'}),
        }


class AddInformationForm(forms.ModelForm):
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
