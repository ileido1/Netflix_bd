from django.urls import path

from . import views

app_name = 'netflixapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('registrarse/', views.registrarse, name='registro'),
]