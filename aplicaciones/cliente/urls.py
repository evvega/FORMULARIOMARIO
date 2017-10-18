from django.conf.urls import url,include
from aplicaciones.adopcion.views import index2
from aplicaciones.adopcion.views import Solicitud,SolicitudList,SolicitudCreate,SolicitudUpdate,SolicitudDelete
from django.contrib.auth.views import login_required


urlpatterns = [

    url(r'^index$',index2),
    url(r'^solicitud/listar$',login_required(SolicitudList.as_view()),name='solicitud_listar'),
    url(r'^solicitud/nueva$',login_required( SolicitudCreate.as_view()), name='solicitud_crear'),
    url(r'^solicitud/editar/(?P<pk>\d+)/',login_required (SolicitudUpdate.as_view()), name='solicitud_editar'),
    url(r'^solicitud/eliminar/(?P<pk>\d+)/', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),

]