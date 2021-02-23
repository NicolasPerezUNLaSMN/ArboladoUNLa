from django.shortcuts import redirect, render
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ProyectoWeb.settings import DATA_COLORES, MAPBOX_ACCESS_TOKEN

from django.forms import modelformset_factory
from .models import Arbol, Imagen, Censo, Coordenada, EstadoDelArbol,Calle
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ImageForm


from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm





def inicio(request):



    return render(request, "ProyectoWebApp/index.html")



def servicios(request):

    #importar todos los objetos de la base de datos
    arboles = Arbol.objects.all()
    


    return render(request, "ProyectoWebApp/services.html", {'arboles':arboles})


def contacto(request):


    return render(request, "ProyectoWebApp/contact.html")


   

def nosotros(request):


    return render(request, "ProyectoWebApp/about.html")



#Por ahora muestro los arboles
def galeria(request):

    #importar todos los objetos de la base de datos
    arboles = Arbol.objects.all()
    imagenes = Imagen.objects.all()

    #galeria es el nombre de la carpeta dentro de templates
    return render(request, "ProyectoWebApp/single.html", {'arboles':arboles, 'imagenes':imagenes})


def estadisticas(request):

  dataEspecies  = [] #Acaguardo las especies sin repetir
  dataEstados = []
  dataAfecto = []


  arboles = Arbol.objects.all().distinct()
  estados = EstadoDelArbol.objects.all().distinct()
  
  #####BLOQUE PARA ESPECIES DISTINTAS
  especie = arboles[0].especie

  for arbol in arboles: #veo cada arbol
    encontrado = False

    for data in dataEspecies: #comparo con cada especie ya guardada
      if (arbol.especie == data):
        encontrado = True
    
    if(encontrado==False): #si no encontre la especie la agrego a la data
      dataEspecies.append(arbol.especie)

  
  #####FIN  ---- BLOQUE PARA ESPECIES DISTINTAS

  ######BLOQUE contar especies
  dataContadorDeEspecies= []
  

  #Recorro las especies
  for data in dataEspecies:
    contador = 0
    for arbol in arboles:  #cuento arboles de esa especie

      if (arbol.especie == data) :
        contador = contador +1

    dataContadorDeEspecies.append(int(contador))

  #############################LO MISMO CON estados sanitarios
  #####BLOQUE PARA ESPECIES DISTINTAS
  estado = estados[0].estadoSanitario

  for e in estados: #veo cada arbol
    encontrado = False

    for data in dataEstados: #comparo con cada especie ya guardada
      if (e.estadoSanitario == data):
        encontrado = True
    
    if(encontrado==False): #si no encontre la especie la agrego a la data
      dataEstados.append(e.estadoSanitario)

   
  #####FIN  ---- BLOQUE PARA ESPECIES DISTINTAS

  ######BLOQUE contar especies
  dataContadorDeEstados= []
  

  #Recorro las especies
  for data in dataEstados:
    contador = 0
    for e in estados:  #cuento arboles de esa especie

      if (e.estadoSanitario == data) :
        contador = contador +1

    dataContadorDeEstados.append(int(contador))


     #############################LO MISMO CON que afecto
  #####BLOQUE PARA ESPECIES DISTINTAS
  afecto = estados[0].afecto

  for e in estados: #veo cada arbol
    encontrado = False

    for data in dataAfecto: #comparo con cada especie ya guardada
      if (e.afecto == data):
        encontrado = True
    
    if(encontrado==False): #si no encontre la especie la agrego a la data
      dataAfecto.append(e.afecto)

   
  #####FIN  ---- BLOQUE PARA ESPECIES DISTINTAS

  ######BLOQUE contar especies
  dataContadorDeAfecto= []
  

  #Recorro las especies
  for data in dataAfecto:
    contador = 0
    for e in estados:  #cuento arboles de esa especie

      if (e.afecto == data) :
        contador = contador +1

    dataContadorDeAfecto.append(int(contador))

  



  diccionario={'especies':dataEspecies, 'cantidades':dataContadorDeEspecies,'estados':dataEstados, 'cantidadesEstados':dataContadorDeEstados,'colores':DATA_COLORES,'afecto':dataAfecto, 'cantidadesAfecto':dataContadorDeAfecto}
 
  print (dataEspecies)
  print (dataContadorDeEspecies)
  print (dataEstados)
  print (dataContadorDeEstados)
  print (dataAfecto)
  print (dataContadorDeAfecto)

  

  return render(request, "ProyectoWebApp/estadisticas.html", diccionario)







def servicioMapa(request):

    #importar todos los objetos de la base de datos
    censos = Censo.objects.all()

 
   
    diccionario = {'censos':censos, 'mapbox_access_token': MAPBOX_ACCESS_TOKEN }

   

    #galeria es el nombre de la carpeta dentro de templates
    return render(request, "ProyectoWebApp/services.html",diccionario)
    #return HttpResponse(json.simplejson.dumps(data), mimetype="application/json")





@login_required(login_url='/login')
def nuevoArbol(request):

   
    ImageFormSet = modelformset_factory(Imagen, form=ImageForm, extra=10, min_num= 1, )
    
    mensajeError = 'Completar los campos marcados con * y enviar una foto como mínimo'

    if request.method == "POST":

      formset = ImageFormSet(request.POST, request.FILES, queryset=Imagen.objects.none())

     


      if formset.is_valid():
        #muestro que datos llegar
        print(request.POST) 

        autor = User()
        autor = request.user


        #Cargamos el censo
        censo = Censo()
        censo.autor = autor
        #Guardamos el censo
        censo.save()


        #Cargamos la calle de ese censo
        calle = Calle()
        calle.censo = censo
        calle.nombre= request.POST['calle']
        calle.numeroFrente=  request.POST.get('numeroDeFrente', 0)
        calle.anchoVereda =request.POST['anchoDeVereda']
        calle.paridad= request.POST.get('paridad',  ' ')
        calle.transito= request.POST.get('transito', ' ')
        #guardado en la base de datos
        calle.save()


        #Cargamos la coordenada de ese censo
        coordenada = Coordenada()
        coordenada.censo = censo
        coordenada.latitud= request.POST['lat']
        coordenada.longitud= request.POST['lon']
        #guardado en la base de datos
        coordenada.save()


        #Cargamos el arbol
        arbol = Arbol()
        arbol.censo = censo
        arbol.especie = request.POST.get('especie', ' ')
        arbol.numeroArbol = request.POST['numeroDeArbol']
        arbol.distanciaEntrePlantas = request.POST['distanciaEntrePlantas']
        arbol.distanciaAlMuro = request.POST['distanciaAlMuro']
        arbol.circunferenciaDelArbol = request.POST['circunferencia']
        arbol.cazuela = request.POST.get('cazuela', ' ' )
        arbol.comentario = request.POST['comentario']
        arbol.altura = request.POST['altura']
        #guardado en la base de datos
        arbol.save()

        #cargo el estado del arbol 
        estadoDelArbol = EstadoDelArbol()
        estadoDelArbol.arbol = arbol
        estadoDelArbol.estadoSanitario = request.POST.get('estadoSanitario', ' ' )
        estadoDelArbol.inclinacion = request.POST.get('inclinacion', ' ' )
        estadoDelArbol.ahuecamiento= request.POST.get('ahuecamiento', ' ' )
        estadoDelArbol.luminaria= request.POST.get('luminaria', ' ' )
        estadoDelArbol.danios= request.POST.get('danios', ' ' )
        estadoDelArbol.veredas= request.POST.get('daniosVereda', ' ' )
        estadoDelArbol.podas= request.POST.get('podas', ' ' )
        estadoDelArbol.cordon= request.POST.get('cordon', ' ' )
        estadoDelArbol.superficieAfectada= request.POST.get('superficieAfectada', 0 )
        estadoDelArbol.afecto= request.POST.get('afecto', ' ' )
        estadoDelArbol.cables= request.POST.get('cables', ' ' )
        estadoDelArbol.raices= request.POST.get('raices', ' ' )
        estadoDelArbol.save()
        
        
        #imagen
        for form in formset.cleaned_data:
                
                  if form:
                      img = form['image']
                      imagen = Imagen()
                      imagen.arbol = arbol
                      imagen.image = img
                      imagen.save()
        
        
        
        return galeria(request)
        
      else:  #imagenes no validas

        mensajeError = '¡¡¡ El formulario no ha sido válido, verifique enviar una imagen como mínimo... !!!'
    
    


    formset = ImageFormSet(queryset=Imagen.objects.none())

    return render(request, "ProyectoWebApp/nuevoArbol.html",  {'formset': formset, 'mensajeError':mensajeError})



def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "ProyectoWebApp/index.html")
    # En otro caso redireccionamos al login
    #return redirect('/login')
    return render(request, "ProyectoWebApp/login.html")


def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "ProyectoWebApp/register.html", {'form': form})

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "ProyectoWebApp/login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')