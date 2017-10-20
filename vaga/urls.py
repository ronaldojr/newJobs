from django.conf.urls import include, url

from . import views

app_name = 'vaga'
urlpatterns = [
    url(r'^pesquisar/$', views.pesquisar, name="pesquisar_vagas"),
    url(r'^listar-vagas/$', views.listar_vagas, name="listar_vagas"),
    url(r'^gerenciar-vagas/$', views.gerenciar_vagas, name="gerenciar_vagas"),
    url(r'^cadastrar-vaga/$', views.cadastrar_vaga, name="cadastrar_vaga"),
    url(r'^editar-vaga/$', views.editar_vaga, name="editar_vaga"),
    url(r'^excluir-vaga/$', views.excluir_vaga, name="excluir_vaga"),
    url(r'^relatorios/$', views.relatorios, name="relatorios"),
    url(r'^candidaturas/$', views.candidaturas, name="listar_candidaturas"),
    url(r'^candidatar/(?P<vaga_id>\d+)/$', views.candidatar, name="candidatar"),
    url(r'^finalizar-candidatura/$', views.finalizar_candidatura, name="finalizar_candidatura"),
    url(r'^editar-candidatura/$', views.editar_candidatura, name="editar_candidatura"),
    url(r'^excluir-candidatura/$', views.excluir_candidatura, name="excluir_candidatura"),
]
