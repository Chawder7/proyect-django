from django.shortcuts import render, get_object_or_404
from .models import Alumnos,ComentarioContacto
from .forms import ComtarioContactoForm
import datetime

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
            comentarios = ComentarioContacto.objects.all()
            return render(request,'registros/comentarios.html',{'comentarios':comentarios})
    form = ComtarioContactoForm()
    return render(request,'registros/contacto.html',{'form' : form})

def comentario(request):
    comentarios=ComentarioContacto.objects.all()
    return render(request,'registros/comentarios.html',{'comentarios':comentarios})

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarElminacion.html'):

    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method=='POST':
        comentario.delete()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentarios.html",{'comentarios':comentarios})
    return render(request, confirmacion,{'object':comentario})

def consultaComentarioindividual(request,id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,"registros/editarComentario.html",{'comentario':comentario})

def editarComentarioContacto(request,id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComtarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentarios.html",{'comentarios':comentarios})
    return render(request,"registros/editarComentario.html",{'comentario':comentario})

def consulta1(request):
    alumnos=Alumnos.objects.filter(carrera="TI")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta2(request):
    alumnos=Alumnos.objects.filter(carrera="TI").filter(turno="Matutino")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta3(request):
    alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta5(request):
    alumnos=Alumnos.objects.filter(nombre__in=["Juan","Ana"])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta6(request):
    fechaI = datetime.date(2024,6,1)
    fechaF = datetime.date(2024,6,30)
    alumnos=Alumnos.objects.filter(created__range=(fechaI,fechaF))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta7(request):
    alumnos = Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})
