from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import Cuenta_Form
from django.forms import modelformset_factory
from netflixapp.models import Cuenta


def index(request):
    return render(request, 'netflixapp/index.html')
def registrarse(request):
    Cuentaformset = modelformset_factory(Cuenta, fields=('nombre_usuario', 'email', 'contrasena', 'nombre', 'apellido','fecha_nacimiento','sexo', 'telefono','fecha_creacion'))
    if request.method == 'POST':
        formset = Cuentaformset(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = Cuentaformset()
    return render(request, 'netflixapp/index.html', {'formset': formset})