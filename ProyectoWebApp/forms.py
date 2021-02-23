from django import forms
from .models import Imagen


 
class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='AGREGAR IMAGEN: ')    

    
    class Meta:
        model = Imagen
        fields = ('image', )