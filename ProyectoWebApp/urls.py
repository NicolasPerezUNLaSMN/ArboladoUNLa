from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('', views.inicio, name="Inicio"),
    path('contacto', views.contacto, name="Contacto"),
    path('galeria', views.galeria, name="Galeria"),
    path('nuevoArbol', views.nuevoArbol, name="NuevoArbol"),
    path('servicioMapa', views.mapbox, name="ServicioMapa"),
    path('estadisticas', views.estadisticas, name="Estadisticas"),
    path('welcome', views.welcome, name="Welcome"),
    path('register', views.register, name="Register"),
    path('login', views.login, name="Login"),
    path('logout', views.logout, name="Logout"),
    path('exportCensos', views.export_csv_censos, name='export_csv_censos'),
    path('exportCoordenadas', views.export_csv_coordenadas, name='export_csv_coordenadas'),
    path('exportArboles', views.export_csv_arboles, name='export_csv_arboles'),
    path('exportEstados', views.export_csv_estados, name='export_csv_estados'),
    path('exportImagenes', views.export_csv_imagenes, name='export_csv_imagenes'),
    path('exportCalles', views.export_csv_calles, name='export_csv_calles'),
    path('exportUsuarios', views.export_csv_usuarios, name='export_csv_usuarios'),
    path('escribir_geojson', views.escribir_geojson, name='escribir_geojson'),
   
 
    
    
    

    

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)