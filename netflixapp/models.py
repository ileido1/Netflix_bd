from django.db import models
from django.forms import ModelForm,DateField
from django import forms

# Create your models here.
class Pais(models.Model):
    nombre= models.CharField(max_length=50)
    descripción= models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre= models.CharField(max_length=50)
    descripción= models.CharField(max_length=50)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
class Cuenta(models.Model):
    nombre_usuario = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    contrasena = models.CharField( max_length=50)
    nombre = models.CharField( max_length=50)
    apellido= models.CharField( max_length=50)
    fecha_nacimiento= models.DateField("Fecha de nacimiento (dd/mm/yyyy)" ,auto_now=False, auto_now_add=False, )
    sexo_choices= [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('N/A', 'No aplica'),
    ]   
    sexo = models.CharField(
        max_length=3,
        choices=sexo_choices,
        default='M',
    )
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField( auto_now=True, auto_now_add=False)

class Perfil(models.Model):
    nombre = models.CharField( max_length=50)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)

class Membresia(models.Model):
   nombre_membresia= models.CharField(max_length=50)
   precio = models.IntegerField()
   cuentas = models.ManyToManyField(Cuenta, through='Subscripcion_cuenta')
   def __str__(self):
      return self.nombre_membresia

class Subscripcion_cuenta(models.Model):
    fecha_inicio= models.DateField(auto_now=True)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    membresia = models.ForeignKey(Membresia, on_delete=models.CASCADE)
    fecha_fin = models.DateField(auto_now=False, auto_now_add=False,null=True)

class Tarjeta(models.Model): 
   numerotarjeta= models.IntegerField(primary_key=True);
   ccv=models.IntegerField(max_length=3)
   vencimiento=models.DateField( auto_now=False, auto_now_add=False)
        
class Subscripcion(models.Model):
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    membresia = models.ForeignKey(Membresia, on_delete=models.CASCADE)
    fecha_pago= models.DateTimeField(auto_now=True, auto_now_add=False)
    fin_servicio= models.DateTimeField( auto_now=False, auto_now_add=False)
    total = models.IntegerField()


class Clasificacion_e(models.Model):
    nombre= models.CharField(max_length=50)
    descripcion= models.CharField( max_length=50)

class Genero(models.Model):
    nombre= models.CharField( max_length=50)





class Persona_Contenido (models.Model):
    NombTrab= models.CharField(max_length=50)
    ApellidoTrab = models.CharField( max_length=50)
    Annio_experiencia = models.DateField( auto_now=False, auto_now_add=False)
    sexo_choices= [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('N/A', 'No aplica'),
        ]   
    sexo = models.CharField(
        max_length=3,
        choices=sexo_choices,
        default='M',
    )
    Es_actor = models.BooleanField()
    Es_director = models.BooleanField()


class Tipo_dispositivo(models.Model):
    nombre= models.CharField(max_length=50)
    descripción= models.CharField(max_length=50)

class Dispositivo(models.Model):
    nombre= models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipo_dispositivo, on_delete=models.CASCADE)



class Idioma(models.Model):
    nombre= models.CharField(max_length=50)



class Contenido(models.Model):
    titulo = models.CharField(max_length=50)
    fecha_estreno = models.DateField( auto_now=False, auto_now_add=False)
    original_netflix = models.BooleanField()
    descripcion = models.CharField(max_length=50)
    duracion= models.CharField(max_length=50, null=True)
    tipo_choices= [
    ('P', 'Pelicula'),
    ('S', 'Serie'),
    ]   
    tipo = models.CharField(
        max_length=2,
        choices=tipo_choices,
        default='P',
    )
    clasificacion_edad = models.ForeignKey(Clasificacion_e, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    generos = models.ManyToManyField(Genero)
    subcripciones = models.ManyToManyField(Subscripcion)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

class Temporada(models.Model):
    descripcion= models.CharField(max_length=50)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)

class Episodio(models.Model):
    nombre =models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    duracion = models.CharField(max_length=50)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)

class Historial(models.Model):
    hora_visualizacion= models.TimeField( auto_now=False, auto_now_add=False)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    hora_finalizacion= models.TimeField( auto_now=False, auto_now_add=False)
    fecha = models.DateField( auto_now=False, auto_now_add=False)
    calificacion = models.IntegerField(default = 0)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    Episodio =  models.ForeignKey(Episodio, on_delete=models.CASCADE, null=True)
    Perfil =  models.ForeignKey(Perfil, on_delete=models.CASCADE)

class Actua(models.Model):
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    persona_contenido = models.ForeignKey(Persona_Contenido, on_delete=models.CASCADE)
    es_protagonista = models.BooleanField()

class Dirige(models.Model):
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    persona_contenido = models.ForeignKey(Persona_Contenido, on_delete=models.CASCADE)
    
class Premio(models.Model):
    nombre =models.CharField( max_length=50)
    contenido = models.ForeignKey(Contenido, on_delete=models.CASCADE)
    ano_ganadora = models.DateField( auto_now=False, auto_now_add=False)


        