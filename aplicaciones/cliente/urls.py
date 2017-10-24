from django.conf.urls import url,include
from aplicaciones.cliente.views import CLIENT_CREATE,CLIENTLIST,ClientUpdate,ClientDelete


urlpatterns = [

    url(r'^registrar',CLIENT_CREATE.as_view(),name='cliente_registrar'),
    url(r'^listar', CLIENTLIST.as_view(), name='cliente_listar'),
    url(r'^editar/(?P<pk>\d+)/$', ClientUpdate.as_view(), name='cliente_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',ClientDelete.as_view(), name='cliente_eliminar'),

]