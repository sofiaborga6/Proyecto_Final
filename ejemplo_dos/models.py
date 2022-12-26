from django.db import models
from django.contrib.auth.admin import User

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)
    publicado_el = models.DateField()
    imagen = models.ImageField(upload_to = "posts", null = "True", blank = True) #en la base de datos se guarda la ruta donde se tiene que ir a buscar la imagen. No la imagen. Hay que crear en setting una ruta media root  donde se van a almacenar las imagenes que van subiendo los usuarios.


#luego de crear la clase tengo que hacer el makemigrations python manage.py makemigration y python manage.py migrate

class Avatar(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name= "avatar" )
    imagen = models.ImageField(upload_to = "avatar", null = "True", blank = True) #en la base de datos se guarda la ruta donde se tiene que ir a buscar la imagen. No la imagen. Hay que crear en setting una ruta media root  donde se van a almacenar las imagenes que van subiendo los usuarios.


class Mensaje(models.Model):
    email = models.EmailField()
    nombre = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)
    enviado_el = models.DateField(auto_now_add=True)
