from django.conf.urls import url,include
from aplicaciones.empresa.views import ENTERPRISE_CREATE


urlpatterns = [

    url(r'^registrarempresa',ENTERPRISE_CREATE.as_view(),name='empresa_registrar'),


]