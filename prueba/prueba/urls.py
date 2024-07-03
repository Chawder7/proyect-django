"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from registros import views as views_reg
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_reg.principal, name="Principal"),
    path('contacto/',views_reg.contacto,name="Contacto"),
    path('formulario/',views.formulario,name="Formulario"),
    path('ejemplo/',views.ejemplo,name="ejemplo"),
    path('registrar/',views_reg.registrar,name="Registrar"),
    path('comentario/',views_reg.comentario,name="Comentario"),
    path('eliminarComentario/<int:id>/', views_reg.eliminarComentarioContacto,name="Eliminar"),
    path('editarComentario/<int:id>/',views_reg.editarComentarioContacto,name="Editar"),
    path('formEditarComentario/<int:id>/',views_reg.consultaComentarioindividual,name="ConsultaIndiv"),
    path('consulta1/',views_reg.consulta1,name="Consultas1"),
    path('consulta2/',views_reg.consulta2,name="Consultas2"),
    path('consulta3/',views_reg.consulta3,name="Consultas3"),
    path('consulta4/',views_reg.consulta4,name="Consultas4"),
    path('consulta5/',views_reg.consulta5,name="Consultas5"),
    path('consulta6/',views_reg.consulta6,name="Consultas6"),
    path('consulta7/',views_reg.consulta7,name="Consultas7"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
