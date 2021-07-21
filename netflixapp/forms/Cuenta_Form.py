from django import forms
from ..models import Cuenta, Membresia,Subscripcion_cuenta, Tarjeta,Perfil

class CuentasForm(forms.ModelForm):
    Membresia = forms.ModelChoiceField(queryset=Membresia.objects.all(), widget=forms.Select(attrs={'class':'form-select'}))
    class Meta:
        model = Cuenta
        fields = ['nombre_usuario','email','contrasena','nombre','apellido','fecha_nacimiento', 'sexo','ciudad']
        widgets={
             'fecha_nacimiento':forms.TextInput(attrs={'type': "date"}),
			 'nombre_usuario':forms.TextInput(attrs={'class':'form-control'}),
			 'nombre':forms.TextInput(attrs={'class':'form-control'}),
			 'email':forms.TextInput(attrs={'class':'form-control'}),
			 'contrasena':forms.TextInput(attrs={'class':'form-control'}),
			 'apellido':forms.TextInput(attrs={'class':'form-control'}),
			 'fecha_nacimiento':forms.TextInput(attrs={'class':'form-control','type': "date"}),
			 'sexo':forms.Select(attrs={'class':'form-select'}),
			 'ciudad':forms.Select(attrs={'class':'form-select'}),


			 
        }
		
class Tarjetaform(forms.ModelForm):
	numerodetarjeta = forms.CharField(label="Numero de tarjeta",widget= forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model = Tarjeta
		fields = [
			'ccv',
			'vencimiento',
	
		]
		labels = {
			'ccv': 'ccv',
			'vencimiento': 'Fecha de vencimiento',
			
		}
		widgets = {
			'ccv':forms.TextInput(attrs={'class':'form-control'}),
			'vencimiento':forms.TextInput(attrs={'type': "date",'class':'form-control'}),
			'numerodetarjeta': forms.TextInput(attrs={'class':'form-control'})
		}
class MembresiaForm(forms.ModelForm):
    
    class Meta:
        model = Membresia
        fields = ['nombre_membresia','precio',]
        widgets = {
			    'ccv':forms.TextInput(attrs={'class':'form-control'}),
			    'vencimiento':forms.TextInput(attrs={'type': "date"})}

class PerfilForm(forms.ModelForm):
    	
	class Meta:
		model = Perfil
		fields = ('nombre',)
		widgets = {
			    'nombre':forms.TextInput(attrs={'class':'form-control'}),
			   }
