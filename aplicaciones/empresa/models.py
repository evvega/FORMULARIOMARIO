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
    TYPE_CITY = models.TextField(max_length=1, choices=CITY)
    ADDRESS = models.CharField(max_length=80)
