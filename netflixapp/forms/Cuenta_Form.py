from django import forms

class Cuenta(forms.Form):
    email = forms.EmailField( required=True)
    contrasena = forms.CharField(label="Contrasena" ,max_length=50, required=True)
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Apellido", max_length=50, required=True)
    fecha= forms.DateField(label="Fecha Nacimiento", required=False)
    telefono = forms.IntegerField(required=False)
