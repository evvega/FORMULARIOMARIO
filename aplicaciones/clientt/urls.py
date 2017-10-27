from django.conf.urls import url,include
from aplicaciones.clientt.views import ClientCreate,ClientList,ClientUpdate,ClientDelete


urlpatterns = [

    url(r'^registrar',ClientCreate.as_view(),name='cliente_registrar'),
    url(r'^listar', ClientList.as_view(), name='cliente_listar'),
    url(r'^editar/(?P<pk>\d+)/$', ClientUpdate.as_view(), name='cliente_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',ClientDelete.as_view(), name='cliente_eliminar'),

]