from django.conf.urls import url

from . import views

app_name = 'usuario'
urlpatterns = [
    url(r'^cadastro/$', views.cadastro, name="cadastro"),
    url(r'^cadastrar/$', views.cadastrar, name="cadastrar"),
    url(r'^cadastrado/$', views.cadastrado, name="cadastrado"),
    url(r'^login/$', views.login, name="login"),
    url(r'^logar/$', views.logar, name="logar"),
    url(r'^logout/$', views.logout, name="logout"),
]
