from django.contrib import admin
from .models import Cuenta, Membresia,Subscripcion_cuenta, Tarjeta, Ciudad, Pais,Subscripcion
# Register your models here.

admin.site.register(Cuenta)
admin.site.register(Membresia)
admin.site.register(Ciudad)
admin.site.register(Pais)
admin.site.register(Subscripcion)