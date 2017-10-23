# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ENTERPRISE(models.Model):
    BUSSINES_NAME = models.CharField(max_length=50)
    NIT = models.IntegerField()
    PHONE = models.IntegerField()
    EMAIL = models.IntegerField()
    CITY = (('BOGOTA', 'Bogotá'), ('MEDELLIN', 'Medellin'), ('BARRANQUILLA', 'Barranquilla'), ('CALI', 'Cali'),
            ('CARTAGEA_DE_INDIAS', 'Cartagena de indias'))
    TYPE_CITY_COMPANY = models.TextField(max_length=1, choices=CITY)
    ADDRESS = models.CharField(max_length=80)

    def __str__(self):
        return '{}'.format(self.NAME)



class ADDINFORMATION(models.Model):
    client2 = models.ForeignKey(ENTERPRISE, null=True, blank=True)

    WAY_TO_PAY =(('TCN','Tarjeta de Crédito Nacional'),('VS','Visa'),('MC','Mastercard'),('AE','American Express'),('DN','Diners'),('TD','Tarjetas Débito'),('CB','Consignación Bancaria'),('PB','Pagos via Baloto'),('EF','Efecty'))
    TYPE_WAYTOPAY = models.TextField(max_length=1,choices=WAY_TO_PAY)
    PRODUCT_QUALIFICATION = (('E','Excelente'),('P','Promedio'),('T','Terrible'))
    TYPE_PRODUCTQUALIFICATION = models.TextField(max_length=1,choices=PRODUCT_QUALIFICATION)
    SERVICE_QUALIFICATION = (('S','Satisfecho'),('N','Neutral'),('I','Insatisfecho'))
    TYPE_SERVICEQUALIFICATION = models.TextField(max_length=1,choices=SERVICE_QUALIFICATION)