from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=3000)
    publicado_el = models.DateField()

#luego de crear la clase tengo que hacer el makemigrations python manage.py makemigration y python manage.py migrate

