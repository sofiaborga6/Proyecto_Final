from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from ejemplo_dos.models import Post
from django.urls import reverse_lazy
from ejemplo_dos.forms import UsuarioForm
from django.contrib.auth.views import  LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin  #para que se logee primero antes de entrar a la vistas
from django.contrib.auth.decorators import  login_required


@login_required #para entrar a la pagina tienen que registrarse

def index(request):
    return render(request, "ejemplo_dos/index.html", {}) #index se usa para referenciar a la pagina de inicio

class PostDetalle(DetailView):
    model = Post

class PostList(ListView):
    model = Post

class  PostCrear(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = '__all__'

class PostBorrar(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")

class PostActualizar(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("ejemplo-dos-listar")
    fields = "__all__"


class UserSignUp(CreateView):
    form_class = UsuarioForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('ejemplo-dos-listar') #convierte el nombre de un pack a una URL

class UserLogIn(LoginView):
    next_page = reverse_lazy('ejemplo-dos-listar')

class UserLogout(LogoutView):
    next_page = reverse_lazy('ejemplo-dos-listar')