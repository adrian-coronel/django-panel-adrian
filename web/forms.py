from django.forms import ModelForm
from .models import *

# ModelForm se utiliza para crear formularios basados en modelos
class AlumnoForm(ModelForm):
  class Meta:
    model= TblAlumno
    #El form contrendra todos los campos del modelo
    fields= '__all__'

class ProfesorForm(ModelForm):
  class Meta:
    model= TblProfesor
    fields= '__all__'