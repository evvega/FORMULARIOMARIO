# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from aplicaciones.cliente.models import CLIENTCREATE
from aplicaciones.cliente.forms import CLIENTFORM

# Create your views here.

class CLIENT(CreateView):
    model = CLIENTCREATE
    form = CLIENTFORM
    template_name = 'cliente/cliente_form.html'


