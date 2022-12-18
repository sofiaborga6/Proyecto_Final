from django.shortcuts import render
from django.views.generic import ListView, CreateView
from ejemplo_dos.models import Post

# Create your views here.
def index(request):
    return render(request, "ejemplo_dos/index.html", {}) #index se usa para referenciar a la pagina de inicio

class PostList(ListView):
    model = Post

class  PostCrear(CreateView):
    model = Post
    success_url = "/ejemplo-dos/listar"
    fields = '__all__'
