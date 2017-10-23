from django.conf.urls import url,include
from aplicaciones.empresa.views import ENTERPRISE_CREATE,ADDINFORMATIONLIST


urlpatterns = [

    url(r'^registrarempresa', ENTERPRISE_CREATE.as_view(),name='empresa_registrar'),
    url(r'^listarempresa', ADDINFORMATIONLIST.as_view(), name='empresa_listar'),

]