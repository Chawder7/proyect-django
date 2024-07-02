from django.shortcuts import render, get_object_or_404
from .models import Alumnos,ComentarioContacto
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