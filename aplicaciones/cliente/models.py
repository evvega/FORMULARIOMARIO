# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class CLIENT(models.Model):
    NAME = models.CharField(max_length=50)
    SURNAMES = models.CharField(max_length=80)
    AGE = models.IntegerField()
    GENDER = (  ('M', 'Masculino'), ('F', 'Femenino'),  ('O', 'Otros'), )
    TYPE_GENDER = models.TextField(max_length=1, choices=GENDER)
    EMAIL = models.CharField(max_length=80)
    PHONE = models.IntegerField()
    CITY = (  ('BOGOTA', 'Bogotá'), ('MEDELLIN', 'Medellin'),  ('BARRANQUILLA', 'Barranquilla'),('CALI','Cali'), ('CARTAGEA_DE_INDIAS','Cartagena de indias') )
    TYPE_CITY = models.TextField(max_length=1, choices=CITY)
    SOCIOECONOMIC_LEVEL = models.IntegerField()
    TICKET= models.IntegerField()

class ADDINFORMATION(models.Model):
    WAY_TO_PAY =(('TCN','Tarjeta de Crédito Nacional'),('VS','Visa'),('MC','Mastercard'),('AE','American Express'),('DN','Diners'),('TD','Tarjetas Débito'),('CB','Consignación Bancaria'),('PB','Pagos via Baloto'),('EF','Efecty'))
    TYPE_WAYTOPAY = models.TextField(max_length=1,choices=WAY_TO_PAY)
    PRODUCT_QUALIFICATION = (('E','Excelente'),('P','Promedio'),('T','Terrible'))
    TYPE_PRODUCTQUALIFICATION = models.TextField(max_length=1,choices=PRODUCT_QUALIFICATION)
    SERVICE_QUALIFICATION = (('S','Satisfecho'),('N','Neutral'),('I','Insatisfecho'))
    TYPE_SERVICEQUALIFICATION = models.TextField(max_length=1,choices=SERVICE_QUALIFICATION)
    client = models.ForeignKey(CLIENT,null=False,blank=True)


