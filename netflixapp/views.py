from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# Create your views here.
from .forms import Cuenta_Form
from django.forms import modelformset_factory, DateField, TextInput
from .models import Cuenta, Subscripcion, Membresia, Subscripcion_cuenta, Perfil, Tarjeta
from django import forms
from django.views.generic import ListView, CreateView, DetailView
import datetime


def index(request):
    return render(request, 'netflixapp/index.html')


def registrarse(request):
    if request.method == 'POST':
        formset = Cuenta_Form.CuentasForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("netflixapp/registrarse/?valido")
    else:
        formset = Cuenta_Form.CuentasForm()
    return render(request, 'netflixapp/registro.html', {'formset': formset})


class CuentaList(ListView):
    model = Cuenta
    template_name = "cuenta_list.html"


class CuentaCreateView(CreateView):
    model = Cuenta
    template_name = "netflixapp/registro.html"
    form_class = Cuenta_Form.CuentasForm
    success_url = reverse_lazy('netflixapp:cuenta-list')


class SusbcripcionListView(ListView):
    model = Subscripcion
    template_name = "susbcripcion_list.html"


class SusbcripcionCreateView(CreateView):
    model = Cuenta
    template_name = 'netflixapp/suscripcion_form.html'
    form_class = Cuenta_Form.CuentasForm
    second_form_class = Cuenta_Form.Tarjetaform
    success_url = reverse_lazy('netflixapp:subscripcion-list')

    def get_context_data(self, **kwargs):
        context = super(SusbcripcionCreateView,
                        self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            solicitud = form.save(commit=False)
            solicitud.persona = Tarjeta.objects.create(numerotarjeta=form2['numerodetarjeta'].value(), ccv=form2['ccv'].value(),vencimiento=form2['vencimiento'].value())
            solicitud.save()
            tipome = Membresia.objects.get(id=form['Membresia'].value())
            ahora = datetime.datetime.utcnow()
            finservicio = ahora + datetime.timedelta(days=30)
            sus = Subscripcion.objects.create(
                cuenta=solicitud, membresia=tipome, tarjeta=solicitud.persona, total=20, fin_servicio=finservicio)
            suscribcion_cuenta = Subscripcion_cuenta.objects.create(
                cuenta=solicitud, membresia=tipome)
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class PerfilModelDetailView(DetailView):
    model = Cuenta
    template_name = 'netflixapp/perfilform.html'

    def get_success_url(self):
        return reverse_lazy('main:article', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfiles'] = Perfil.objects.all().filter(cuenta=self.kwargs['pk'])
        context['form'] = Cuenta_Form.PerfilForm
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = Cuenta_Form.PerfilForm(request.POST, request.FILES)
        if form.is_valid():
            perfil=Perfil.objects.create(nombre=form['nombre'].value(), cuenta = Cuenta.objects.get(id=self.kwargs['pk']))
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = Cuenta_Form.PerfilForm
            return self.render_to_response(context=context)

        else:
            self.object = self.get_object()
            context = super().get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context=context)
