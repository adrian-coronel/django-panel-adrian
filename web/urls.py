from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    # Principal punto de entrada para un proceso de solicitud-respuesta.
    path('', views.AlumnoView.as_view(),name='index'),
    path('profesores/', views.ProfesorView.as_view(),name='index_profesores'),
    # path('delete-alumno/', views.AlumnoView., name='delete_alumno')
]