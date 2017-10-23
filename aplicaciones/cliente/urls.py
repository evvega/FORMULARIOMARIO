from django.conf.urls import url,include
from aplicaciones.cliente.views import CLIENT_CREATE,CLIENTLIST


urlpatterns = [

    url(r'^registrar',CLIENT_CREATE.as_view(),name='cliente_registrar'),
    url(r'^listar', CLIENTLIST.as_view(), name='cliente_listar'),

]