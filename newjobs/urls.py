from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^', include('core.urls', namespace='core')),
    url(r'^usuario/', include('usuario.urls', namespace='usuario')),
    url(r'^vaga/', include('vaga.urls', namespace='vaga')),
    url(r'^admin/', admin.site.urls),
]
