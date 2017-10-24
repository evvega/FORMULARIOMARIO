# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from aplicaciones.cliente.models import CLIENT,ADDINFORMATION
from aplicaciones.cliente.forms import CLIENTFORM,ADDINFORMATIONFORM
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class CLIENT_CREATE(CreateView):
    model = ADDINFORMATION
    form_class = ADDINFORMATIONFORM
    second_form_class = CLIENTFORM
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_listar')



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
            registro.client1 = form2.save()
            registro.save()
            return HttpResponseRedirect(self.get_success_url())
        else:

            return self.render_to_response(self.get_context_data(form=form,form2=form2))

class CLIENTLIST(ListView):
    model = ADDINFORMATION
    template_name = 'cliente/cliente_list.html'

class ClientUpdate(UpdateView):
    model = ADDINFORMATION
    second_model = CLIENT
    template_name = 'cliente/cliente_form.html'
    form_class= ADDINFORMATIONFORM
    second_form_class= CLIENTFORM
    success_url = reverse_lazy('cliente:cliente_listar')


    def get_context_data(self, **kwargs):
        context = super(ClientUpdate,self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        addinformation=self.model.objects.get(id=pk)
        cliente= self.second_model.objects.get(id=addinformation.client1_id)
        if 'form' not in context:
            context['form']=self.form_class(instance=addinformation)
        if 'form2' not in context:
            context['form2']=self.second_form_class(instance=cliente)
        context['id']=pk
        return context
    def post(self, request, *args, **kwargs):
        self.object=self.get_object
        id_addinformation= kwargs['pk']
        addinformation=self.model.objects.get(id=id_addinformation)
        cliente=self.second_model.objects.get(id=addinformation.client1_id)
        form=self.form_class(request.POST, instance=addinformation)
        form2 = self.second_form_class(request.POST, instance=cliente)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class ClientDelete(DeleteView):

    model = ADDINFORMATION
    template_name ='cliente/cliente_delete.html'