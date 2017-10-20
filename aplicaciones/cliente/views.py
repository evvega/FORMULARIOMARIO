# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from aplicaciones.cliente.models import CLIENT
from aplicaciones.cliente.forms import CLIENTFORM,ADDINFORMATIONFORM
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class CLIENT_CREATE(CreateView):
    model = CLIENT
    form_class = CLIENTFORM
    second_form_class = ADDINFORMATIONFORM
    template_name = 'clientesito/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_registrar')


    def get_context_data(self, **kwargs):
        context = super(CLIENT_CREATE,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form']= self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2']= self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(self.request.POST)
        form2 =self.second_form_class(self.request.POST)
        if form.is_valid() and form2.is_valid():
            registro = form.save(commit=False)
            registro.client = form2.save()
            registro.save()
            return HttpResponseRedirect(self.get_success_url())
        else:

            return self.render_to_response(self.get_context_data(form=form,form2=form2))






