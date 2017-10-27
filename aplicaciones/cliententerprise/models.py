# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Enterprise(models.Model):
    BUSSINES_NAME = models.CharField(max_length=50)
    NIT = models.CharField(max_length=50)
    PHONE = models.IntegerField()
    EMAIL = models.EmailField()
    CITY = (('BOGOTA', 'Bogotá'), ('MEDELLIN', 'Medellin'), ('BARRANQUILLA', 'Barranquilla'), ('CALI', 'Cali'),
            ('CARTAGEA_DE_INDIAS', 'Cartagena de indias'))
    TYPE_CITY_COMPANY = models.TextField(max_length=1, choices=CITY)
    ADDRESS = models.CharField(max_length=80)
    TICKET = models.IntegerField()


    def __str__(self):
        return '{}'.format(self.BUSSINES_NAME)



class AddInformation(models.Model):

    client2 = models.ForeignKey(Enterprise,on_delete=models.CASCADE, null=True, blank=True)
    WAY_TO_PAY =(('TARJETADECREDITONACIONAL','Tarjeta de Crédito Nacional'),('VISA','Visa'),('MASTERCARD','Mastercard'),('AMERICANEXPRESS','American Express'),('DINERS','Diners'),('TARJETASDEBITO','Tarjetas Débito'),('CONSIGNACIONBANCARIA','Consignación Bancaria'),('PAGOSVIABALOTO','Pagos via Baloto'),('EFECTY','Efecty'))
    TYPE_WAYTOPAY = models.TextField(max_length=1,choices=WAY_TO_PAY)
    PRODUCT_QUALIFICATION = (('5','Excelente'),('3','Promedio'),('1','Terrible'))
    TYPE_PRODUCTQUALIFICATION = models.TextField(max_length=1,choices=PRODUCT_QUALIFICATION)
    SERVICE_QUALIFICATION = (('5','Satisfecho'),('3','Neutral'),('1','Insatisfecho'))
    TYPE_SERVICEQUALIFICATION = models.TextField(max_length=1,choices=SERVICE_QUALIFICATION)