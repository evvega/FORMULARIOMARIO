# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import CreateView,UpdateView,ListView,DeleteView
from aplicaciones.empresa.models import Enterprise,AddInformation
from aplicaciones.empresa.forms import ADDINFORMATIONFORM,ENTERPRISEFORM
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

class EnterpriseCreate(CreateView):
    model =AddInformation
    form_class = ADDINFORMATIONFORM
    second_form_class = ENTERPRISEFORM
    template_name = 'empresa/empresa_form.html'
    success_url = reverse_lazy('empresa:empresa_listar')

    def get_context_data(self, **kwargs):
        context = super(EnterpriseCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(self.request.POST)
        form2 = self.second_form_class(self.request.POST)
        if form.is_valid() and form2.is_valid():
            registro = form.save(commit=False)
            registro.client2 = form2.save()
            registro.save()
            return HttpResponseRedirect(self.get_success_url())
        else:

            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class AddInformationList(ListView):
    model = AddInformation
    template_name = 'empresa/empresa_list.html'


class EnterpriseUpdate(UpdateView):
    model = AddInformation
    second_model = Enterprise
    template_name = 'empresa/empresa_form.html'
    form_class= ADDINFORMATIONFORM
    second_form_class= ENTERPRISEFORM
    success_url = reverse_lazy('empresa:empresa_listar')


    def get_context_data(self, **kwargs):
        context = super(EnterpriseUpdate,self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk',0)
        addinformation=self.model.objects.get(id=pk)
        empresa= self.second_model.objects.get(id=addinformation.client2_id)
        if 'form' not in context:
            context['form']=self.form_class(instance=addinformation)
        if 'form2' not in context:
            context['form2']=self.second_form_class(instance=empresa)
        context['id']=pk
        return context
    def post(self, request, *args, **kwargs):
        self.object=self.get_object
        id_addinformation= kwargs['pk']
        addinformation=self.model.objects.get(id=id_addinformation)
        empresa=self.second_model.objects.get(id=addinformation.client2_id)
        form=self.form_class(request.POST, instance=addinformation)
        form2 = self.second_form_class(request.POST, instance=empresa)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

class EnterpriseDelete(DeleteView):

    model = AddInformation
    template_name ='empresa/empresa_delete.html'
    success_url = reverse_lazy('empresa:empresa_listar')
