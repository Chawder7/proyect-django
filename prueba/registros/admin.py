from typing import Any
from django.contrib import admin
from django.http import HttpRequest
from .models import Alumnos, Comentario, ComentarioContacto,Archivos


# Register your models here.
class AdministrarMdoelo(admin.ModelAdmin):
    readonly_fields=('created','update')
    list_display = ('matricula','nombre','carrera','turno','imagen')
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Usuarios").exists():
            return('matricula','carrera','turno')
        else:
            return('created','update')
admin.site.register(Alumnos, AdministrarMdoelo)

class AdminComentario(admin.ModelAdmin):
    list_display = ('id','coment')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created','id')

admin.site.register(Comentario, AdminComentario)

class AdminContacto(admin.ModelAdmin):
    list_display = ('id','usuario','mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created','id')

admin.site.register(ComentarioContacto, AdminContacto)

class AdminArchivos(admin.ModelAdmin):
    list_display = ('id','titulo')
admin.site.register(Archivos,AdminArchivos)

