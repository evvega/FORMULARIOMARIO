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
    CITY = models.CharField(max_length=80)
    SOCIOECONOMIC_LEVEL = models.IntegerField()
    TICKET= models.IntegerField()


