from django.urls import path
from . import views
from netflixapp.views import CuentaList, CuentaCreateView, SusbcripcionListView, SusbcripcionCreateView,PerfilModelDetailView

app_name = 'netflixapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('cuenta/', SusbcripcionCreateView.as_view(), name='registroc'),
    path('cuentas/', SusbcripcionListView.as_view(), name='subscripcion-list'),
    path('cuenta/<int:pk>', PerfilModelDetailView.as_view(), name='perfil-detail'),
]