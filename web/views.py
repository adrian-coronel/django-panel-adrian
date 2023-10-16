from django.shortcuts import render, redirect
from django.http import HttpResponse

# importamos la clase View
from django.views import View
from .models import *
from .forms import *


# Create your views here.
class AlumnoView(View):
    
    def get(self,request):
        listaAlumnos = TblAlumno.objects.all()
        form = AlumnoForm()
        context = {
            'alumnos' : listaAlumnos,
            'form': form,
            'titulo': 'Alumnos',
            'btnCreate': 'Nuevo Alumno',
            'urlText': 'web:index'
        }
        return render(request,'index.html',context)

    def post(self, request):
        formAlumno = AlumnoForm(request.POST)
        if 'id' in formAlumno.data:
            alumno_id = formAlumno.data['id']
            # Verifica si se proporcionó un ID y elimina al alumno si es válido
            try:
                alumno = TblAlumno.objects.get(alumno_id=alumno_id)
                alumno.delete()
                return redirect('/')
            except TblAlumno.DoesNotExist:
                # Maneja el caso en el que no se encuentre el alumno
                pass

        if formAlumno.is_valid():            
            formAlumno.save()
        return redirect('/')

class ProfesorView(View):
    def get(self,request):
        listaProfesores = TblProfesor.objects.all()
        form = ProfesorForm()
        context = {
            'profesores' : listaProfesores,
            'form': form,
            'titulo': 'Profesores',
            'btnCreate': 'Nuevo Profesor',
            'urlText': 'web:index_profesores'
        }
        return render(request,'index.html',context)

    def post(self, request):
        formProfesor = ProfesorForm(request.POST)
        if 'id' in formProfesor.data:
            profesor_id = formProfesor.data['id']
            # Verifica si se proporcionó un ID y elimina al alumno si es válido
            try:
                profesor = TblProfesor.objects.get(profesor_id=profesor_id)
                profesor.delete()
                return redirect('/profesores')
            except TblProfesor.DoesNotExist:
                # Maneja el caso en el que no se encuentre el alumno
                pass
        if formProfesor.is_valid():            
            formProfesor.save()
        return redirect('/profesores')
