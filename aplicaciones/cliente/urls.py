from django.conf.urls import url,include
from aplicaciones.cliente.views import CLIENT_CREATE


urlpatterns = [

    url(r'^registrar',CLIENT_CREATE.as_view(),name='cliente_registrar'),


]