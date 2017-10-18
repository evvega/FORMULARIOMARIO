# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class CLIENTCREATE(models.Model):
    NAME =models.CharField(max_length=50)
    SURNAMES = models.CharField(max_length=80)
    GENDER = (
        ('M', 'MASCULINO'),
        ('F', 'FEMENINO'),
        ('O', 'OTROS'),
    )
    TYPE_GENDER = models.CharField(max_length=1, choices=GENDER)
    EDAD = models.IntegerField
    