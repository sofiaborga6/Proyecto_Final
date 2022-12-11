from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar, FamiliarForm    
from django.views import View

def index(request):
    return render(request, "ejemplo/saludar.html")

def saludar_a(request, nombre):
    return render(request,
    "ejemplo/saludar_a.html",
    {"nombre": nombre}
    )

def sumar(request, a, b):
    return render(request, "ejemplo/sumar.html",
    {"a": a,
    "b": b,
    "resultado": a + b
    }
    )

def buscar(request):
    lista_de_nombre = ["SOFIA", "LILIANA", "ANDREA"]
    query = request.GET['q']

    if query in lista_de_nombre:
        indice_de_resultados = lista_de_nombre.index(query)
        resultados = lista_de_nombre[indice_de_resultados]
    else:
        resultados = "no hay match"

    return render(request, 'ejemplo/buscar.html', {"resultados": resultados})

def monstrar_familiares(request):
  lista_familiares = Familiar.objects.all()
  return render(request, "ejemplo/familiares.html", {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid(): ##valida que se esten tomando la cantidad de caracteres correctos
            nombre = form.cleaned_data.get("nombre") ##limpia datos que los necesita python pero que no queremos mostrar.
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})