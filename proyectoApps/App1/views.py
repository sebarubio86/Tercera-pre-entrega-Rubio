from django.shortcuts import render
from App1.models import *
from django.http import HttpResponse
from App1.forms import *

# Create your views here.
def inicio(request):
    return render(request, 'App1/inicio.html')

def medicos(request):
    return render(request,'App1/medicos.html')

def pacientes(request):
    return render(request,'App1/pacientes.html')

def turnos(request):
    return render(request,'App1/turnos.html')

#------------------------ FORMULARIOS ------------------------
def medicoFormulario(request):
    if request.method == "POST":
        miFormulario = MedicoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            asdasd = Medico(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']), informacion['email'], informacion['especialidad'])
            asdasd.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario = MedicoFormulario()

    return render(request, "App1/medicoFormulario.html", {"miFormulario": miFormulario})


def pacienteFormulario(request):
    if request.method == "POST":
        miFormulario = PacienteFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            asdasd = Paciente(int(informacion['id']),str(informacion['nombre']),str(informacion['apellido']), informacion['email'], informacion['dni'])
            asdasd.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario = PacienteFormulario()

    return render(request, "App1/pacienteFormulario.html", {"miFormulario": miFormulario})


def turnoFormulario(request):
    if request.method == "POST":
        miFormulario = TurnoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
        
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            asdasd = Turno(int(informacion['id']),str(informacion['dni']),str(informacion['fecha']), informacion['apellido'],)
            asdasd.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario = TurnoFormulario()

    return render(request, "App1/turnoFormulario.html", {"miFormulario": miFormulario})


def leerMedicos(request):
    medicos= Medico.objects.all() # trae a todos los medicos
    contexto= {"medicos": medicos}
    return render(request, "App1/leerMedicos.html",contexto)

def leerPacientes(request):
    pacientes= Paciente.objects.all() # trae a todos los pacientes
    contexto= {"pacientes": pacientes}
    return render(request, "App1/leerPacientes.html",contexto)

def leerTurnos(request):
    turnos= Turno.objects.all() # trae a todos los turnos
    contexto= {"turnos": turnos}
    return render(request, "App1/leerTurnos.html",contexto)


#----------------------------------------------------------
def busquedaMedico(request):
    return render(request,'App1/buscarMedicos.html')


def buscar(request):
    if request.GET['medico']:
        medico = request.GET['medico']
        medicos= Medico.objects.filter(nombre__icontains=medico)

        return render(request,'App1/resultadoBusqueda.html', {"medicos":medicos,})
    else:
        respuesta= "No enviaste datos"

    return HttpResponse(respuesta)