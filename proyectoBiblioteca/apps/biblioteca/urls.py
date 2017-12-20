from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.VistaIndex, name='index'),
    url(r'^buscar/$', views.buscar, name='buscar')
]
