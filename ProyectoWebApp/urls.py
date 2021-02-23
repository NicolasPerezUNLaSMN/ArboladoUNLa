from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('', views.inicio, name="Inicio"),
    path('contacto', views.contacto, name="Contacto"),
    path('galeria', views.galeria, name="Galeria"),
    path('nuevoArbol', views.nuevoArbol, name="NuevoArbol"),
    path('servicioMapa', views.servicioMapa, name="ServicioMapa"),
    path('estadisticas', views.estadisticas, name="Estadisticas"),
    path('welcome', views.welcome, name="Welcome"),
    path('register', views.register, name="Register"),
    path('login', views.login, name="Login"),
    path('logout', views.logout, name="Logout"),

    

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)