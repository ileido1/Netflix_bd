from django.contrib import admin
from django.urls import include, path
from netflixapp import views

urlpatterns = [
    path('netflixapp/', include('netflixapp.urls')),
    path('admin/', admin.site.urls),
]
