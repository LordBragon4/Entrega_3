from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Rescatado
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import RegistroUForm, LoginForm, RescatadoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import generics 
from .serializers import RescatadoSerializer

# Vistas iniciales.
def index(request):
    rescatados = Rescatado.objects.filter(estado="Rescatado").order_by('nombre')
    disponibles = Rescatado.objects.filter(estado="Disponible").order_by('nombre')
    adoptados = Rescatado.objects.filter(estado="Adoptado").order_by('nombre')
    return render(request, 'web_misperris/index.html',{'rescatados': rescatados, 'disponibles': disponibles, 'adoptados': adoptados})


def formulario(request):
    form = RegistroUForm()
    if request.method == "POST":
        form = RegistroUForm(request.POST)
        if form.is_valid():
            Usuario=form.save(commit=False)
            Usuario.tipo_usuario = "adoptante"
            Usuario.save()
            return redirect('registrado',Usuario.run)
    else:
        form = RegistroUForm()
    return render(request, 'web_misperris/formulario.html', {'form': form})

def registrado(request,pk):
    user = get_object_or_404(Usuario, run=pk)

    return render(request,'web_misperris/registrado.html',{'user':user})

def login(request):
    if request.method == "POST":
        try:
            User = Usuario.objects.get(run=request.POST.get('run'),password=request.POST.get('password'))
        except Usuario.DoesNotExist:
            User = None
        if User is not None:
            if User.tipo_usuario == "adoptante":
              return redirect('usuario')
            else:
                return redirect('rescatado_list')
        else: return redirect('login')
        
    return render(request,'web_misperris/login.html',{})


#VISTAS DEL ADMINISTRADOR (CRUD)
class RescatadoList(ListView):
    model = Rescatado
    template_name = 'web_misperris/rescatado_list.html'
    
class RescatadoListD(ListView):
    model = Rescatado
    template_name = 'web_misperris/rescatado_list.html'
    queryset = Rescatado.objects.filter(estado = 'Disponible')


class RescatadoListR(ListView):
    model = Rescatado
    template_name = 'web_misperris/rescatado_list.html'
    queryset = Rescatado.objects.filter(estado = 'Rescatado')


class RescatadoListA(ListView):
    model = Rescatado
    template_name = 'web_misperris/rescatado_list.html'
    queryset = Rescatado.objects.filter(estado = 'Adoptado')


class RescatadoCreate(CreateView):
    model = Rescatado
    form_class = RescatadoForm
    template_name = 'web_misperris/rescatado_create.html'
    success_url = reverse_lazy('rescatado_list')

class RescatadoUpdate(UpdateView):
    model = Rescatado
    form_class = RescatadoForm
    template_name = 'web_misperris/rescatado_create.html'
    success_url = reverse_lazy('rescatado_list')

class RescatadoDelete(DeleteView):
    model = Rescatado
    template_name = 'web_misperris/rescatado_delete.html'
    success_url = reverse_lazy('rescatado_list')



#VISTAS DEL USUARIO (LISTA DE PERROS DISPONIBLES)
class usuario(ListView):
    model = Rescatado
    template_name = 'web_misperris/rescatado_list2.html'
    queryset = Rescatado.objects.filter(estado = 'Disponible')
	
	
#API
class RescatadoList(generics.ListCreateAPIView):
	queryset = Rescatado.objects.all()
	serializer_class = RescatadoSerializer

class RescatadoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Usuario.objects.all()
	serializer_class = RescatadoSerializer 
		

	



