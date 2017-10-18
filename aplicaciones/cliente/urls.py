from django.conf.urls import url,include
from aplicaciones.cliente.views import CLIENT


urlpatterns = [

    url(r'^cliente/formulario',CLIENT.as_view(),name='cliente_formulario'),


]