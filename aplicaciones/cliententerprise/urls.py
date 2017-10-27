from django.conf.urls import url,include
from aplicaciones.cliententerprise.views import EnterpriseCreate,AddInformationList,EnterpriseUpdate,EnterpriseDelete


urlpatterns = [

    url(r'^registrarempresa', EnterpriseCreate.as_view(),name='empresa_registrar'),
    url(r'^listarempresa', AddInformationList.as_view(), name='empresa_listar'),
    url(r'^editar/(?P<pk>\d+)/$', EnterpriseUpdate.as_view(), name='empresa_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$',EnterpriseDelete.as_view(), name='empresa_eliminar'),

]