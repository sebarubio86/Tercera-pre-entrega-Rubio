from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    dni= models.IntegerField()
    def __str__(self):
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | E-mail: {self.email} | DNI: {self.dni}"

class Medico(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    especialidad= models.CharField(max_length=30)
    def __str__(self):
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | E-mail: {self.email} | Profesión: {self.especialidad}"

class Turno(models.Model):
    dniPaciente= models.IntegerField()
    fecha= models.DateField()
    apellidoMedico= models.CharField(max_length=30)
    def __str__(self):
        return f"DNI Paciente: {self.dniPaciente} | Fecha: {self.fecha} | Medico: {self.apellidoMedico}"
