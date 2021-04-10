from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.


#-----------------------------------------CLASE------------------------------
class Censo(models.Model):
    
    created= models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now_add=True)

    #Un usuario tiene muchos Censos
    autor=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(arbol):
        return '%s;%s;%s' %(arbol.pk, arbol.created, arbol.updated)

    class Meta:
        verbose_name = "Censo"
        verbose_name_plural ="Censos"


#-----------------------------------------CLASE------------------------------
class Calle(models.Model):

    

    nombre= models.CharField(max_length=50, null=True, blank=True)
    numeroFrente= models.IntegerField(default= -1,null=True, blank=True)
    anchoVereda =models.FloatField(default= -1,null=True, blank=True)
    paridad= models.CharField(max_length=50, null=True, blank=True)
    transito= models.CharField(max_length=50, null=True, blank=True)


    #relacion
    censo = models.OneToOneField(Censo,on_delete=models.CASCADE,primary_key=True,blank=True)

    def __str__(arbol):
        return '%s;%s;%s;%s;%s;%s' %(arbol.nombre,arbol.numeroFrente,arbol.anchoVereda, arbol.paridad,arbol.transito, arbol.censo.pk)

    class Meta:
        verbose_name = "Calle"
        verbose_name_plural ="Calles"

#-----------------------------------------CLASE------------------------------
class Coordenada(models.Model):


   

    latitud=models.FloatField(default= -1)
    longitud=models.FloatField(default= -1)

     #relacion
    censo = models.OneToOneField(Censo,on_delete=models.CASCADE,primary_key=True,blank=True)

    def __str__(arbol):
        return '%s;%s;%s' %(arbol.latitud, arbol.longitud, arbol.censo.pk)

    class Meta:
        verbose_name = "Coordenada"
        verbose_name_plural ="Coordenadas"

#-----------------------------------------CLASE------------------------------
class Arbol(models.Model):

    

    especie = models.CharField(max_length=50)
    numeroArbol = models.IntegerField(default= -1)
    distanciaEntrePlantas = models.FloatField(default= -1,null=True, blank=True)
    distanciaAlMuro = models.FloatField(default= -1,null=True, blank=True)
    altura = models.FloatField(default= -1,null=True, blank=True)
    circunferenciaDelArbol = models.FloatField()
    cazuela = models.CharField(max_length=50)
    comentario = models.CharField(max_length=200)

    #relacion
    censo = models.OneToOneField(Censo,on_delete=models.CASCADE,primary_key=True,blank=True)

    def __str__(arbol):
        return '%s;%s;%s;%s;%s;%s;%s;%s;%s;%s' %(arbol.pk, arbol.especie,arbol.numeroArbol, arbol.distanciaEntrePlantas,
         arbol.distanciaAlMuro, arbol.altura, arbol.circunferenciaDelArbol, arbol.cazuela, arbol.comentario, arbol.censo.pk)

    #imagen=models.ImageField()
    class Meta:
        verbose_name = "Arbol"
        verbose_name_plural ="Arboles"



#-----------------------------------------CLASE------------------------------
class EstadoDelArbol(models.Model):


    

    estadoSanitario = models.CharField(max_length=50, null=True, blank=True)
    inclinacion = models.CharField(max_length=50, null=True, blank=True)
    ahuecamiento= models.CharField(max_length=50, null=True, blank=True)
    luminaria= models.CharField(max_length=50, null=True, blank=True)
    danios= models.CharField(max_length=50, null=True, blank=True)
    veredas= models.CharField(max_length=50, null=True, blank=True)
    podas= models.CharField(max_length=50, null=True, blank=True)
    cordon = models.FloatField(null=True, blank=True)
    superficieAfectada = models.IntegerField(null=True, blank=True)
    afecto= models.CharField(max_length=50, null=True, blank=True)
    cables= models.CharField(max_length=50, null=True, blank=True)
    raices = models.CharField(max_length=50, null=True, blank=True)


        #relacion
    arbol = models.OneToOneField(Arbol,on_delete=models.CASCADE,primary_key=True,blank=True)

    def __str__(arbol):
        return '%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s' %(arbol.estadoSanitario,arbol.inclinacion, arbol.ahuecamiento, arbol.luminaria, arbol.danios
        ,arbol.veredas, arbol.podas, arbol.cordon, arbol.superficieAfectada, arbol.afecto, arbol.cables, arbol.raices, arbol.arbol.pk)


    class Meta:
        verbose_name = "EstadoSanitario"
        verbose_name_plural ="EstadosSanitarios"

#-----------------------------------------CLASE------------------------------

def get_image_filename(instance, filename):
    title =  'titulo'
    slug = slugify(title)
    return "imagenesArboles/%s-%s" % (slug, filename)  


class Imagen(models.Model):

    #img = models.ImageField(upload_to='imagenesArboles')
    

    #relacion
    arbol = models.ForeignKey(Arbol, on_delete=models.CASCADE, null=True,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to=get_image_filename,verbose_name='Image')

    def __str__(arbol):
        return '%s;%s;%s' %(arbol.pk, arbol.image, arbol.arbol.pk)

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural ="Imagenes"


 
