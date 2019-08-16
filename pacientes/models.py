from django.db import models
from django.utils import timezone




class Paciente(models.Model):
    doctor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cedula=models.CharField(max_length=10)
    Nombre = models.CharField(max_length=100)
    preg = models.IntegerField()
    plas = models.IntegerField()
    press = models.IntegerField()
    skin = models.IntegerField()
    test = models.IntegerField()
    mass = models.DecimalField(max_digits=100,decimal_places=1)
    pedi = models.DecimalField(max_digits=10,decimal_places=3)
    age = models.IntegerField()
    porcentaje=models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    date = models.DateTimeField(default=timezone.now)

class PacienteDB(models.Model):
    preg = models.IntegerField()
    plas = models.IntegerField()
    press = models.IntegerField()
    skin = models.IntegerField()
    test = models.IntegerField()
    mass = models.DecimalField(max_digits=100,decimal_places=1)
    pedi = models.DecimalField(max_digits=10,decimal_places=3)
    age = models.IntegerField()
    clase=models.IntegerField()

