from django.contrib import admin
from .models import Alumnos

# Register your models here.
class AdministrarMdoelo(admin.ModelAdmin):
    readonly_fields=('created','update')

admin.site.register(Alumnos, AdministrarMdoelo)