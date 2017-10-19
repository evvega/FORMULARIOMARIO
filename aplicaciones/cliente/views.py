# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from aplicaciones.cliente.models import CLIENT
from aplicaciones.cliente.forms import CLIENTFORM
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class CLIENT_CREATE(CreateView):
    model = CLIENT
    form_class = CLIENTFORM
    template_name = 'clientesito/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_registrar')




