from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from curso.models import Post
from django.urls import reverse_lazy
from curso.forms import UsuarioForm
from django.contrib.auth.views import  LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin  #para que se logee primero antes de entrar a la vistas
from django.contrib.auth.decorators import  login_required
from curso.models import Avatar, Post, Mensaje
from django.contrib.auth.admin import User 
from django.contrib.messages.views import SuccessMessageMixin


@login_required #para entrar a la pagina tienen que registrarse

def index(request):
    posts = Post.objects.order_by('publicado_el').all()
    return render(request, "curso/index.html", {"posts": posts}) #index se usa para referenciar a la pagina de inicio

class PostDetalle(DetailView):
    model = Post

class PostList(ListView):
    model = Post

class  PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("curso-listar")
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("curso-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("curso-listar")
    fields = "__all__"


class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('curso-listar') #convierte el nombre de un pack a una URL

class UserLogIn(LoginView):
    next_page = reverse_lazy('curso-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('curso-listar')

class AvatarActualizar(UpdateView):
    model = Avatar
    fields = ['imagen']
    success_url = reverse_lazy('curso-listar')

class UserActualizar(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email')
    success_url = reverse_lazy('curso-listar')

class MensajeDetalle(DetailView):
    model = Mensaje

class MensajeListar(LoginRequiredMixin, ListView):
    model = Mensaje  

class MensajeCrear(SuccessMessageMixin, CreateView):
    model = Mensaje
    success_url = reverse_lazy("curso-mensajes-crear")
    fields = ['nombre', 'email', 'texto']
    success_message = "Mensaje de contacto enviado!!"

class MensajeBorrar(LoginRequiredMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("curso-mensajes-listar")