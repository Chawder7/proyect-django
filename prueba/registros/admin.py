from django.contrib import admin
from .models import Alumnos, Comentario, ComentarioContacto


# Register your models here.
class AdministrarMdoelo(admin.ModelAdmin):
    readonly_fields=('created','update')
    list_display = ('matricula','nombre','carrera','turno','imagen')
    search_fields = ('matricula','nombre','carrera','turno')
    date_hierarchy = 'created'
    list_filter = ('carrera','turno')
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

