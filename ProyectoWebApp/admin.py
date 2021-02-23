from django.contrib import admin
from ProyectoWebApp.models import Censo, Coordenada, Arbol, EstadoDelArbol, Imagen

# Register your models here.
admin.site.register(Censo)
admin.site.register(Coordenada)
admin.site.register(Arbol)
admin.site.register(EstadoDelArbol)
admin.site.register(Imagen)