from django.urls import path
from App1 import views 
urlpatterns = [

    path('', views.inicio, name="Inicio"), #este era nuestro primer view
    path('medicos', views.medicos, name="Medicos"),
    path('pacientes', views.pacientes, name="Pacientes"),
    path('turnos', views.turnos, name="Turnos"),
    
    path('medicoFormulario', views.medicoFormulario, name="MedicoFormulario"),
    path('pacienteFormulario', views.pacienteFormulario, name="PacienteFormulario"),
    path('turnoFormulario', views.turnoFormulario, name="TurnoFormulario"),

    path('leerMedicos',views.leerMedicos,name='LeerMedicos'),
    path('leerPacientes',views.leerPacientes,name='LeerPacientes'),
    path('leerTurnos',views.leerTurnos,name='LeerTurnos'),

    path('buscarMedicos',views.busquedaMedico,name="BuscarMedicos"),
    path('buscar/',views.buscar),
]