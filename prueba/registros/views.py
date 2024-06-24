from django.shortcuts import render
from .models import Alumnos
from .forms import ComtarioContactoForm

# Create your views here.
def principal(request):
    alumnos=Alumnos.objects.all()
    return render(request,'registros/principal.html',{'alumnos':alumnos})

def contacto(request):
    return render(request,'registros/contacto.html')

def registrar(request):
    if request.method == 'POST':
        form = ComtarioContactoForm(request.POST)
        if form.is_valid:
            form.save()
            return render(request,'registros/contacto.html')
    form = ComtarioContactoForm()
    return render(request,'registros/contacto.html',{'form' : form})