import os

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import PacienteForm
from django.shortcuts import redirect
import pandas as pd
import sqlite3
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.model_selection import train_test_split
import numpy as np
from pacientes.models import Paciente

from django.db import models
from sklearn.externals import joblib

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')
def paciente_new(request):

    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            paciente.doctor = request.user
            logreg = joblib.load("modelo.sav")
            X_new= np.array([paciente.preg,paciente.plas,paciente.press,paciente.skin,paciente.test,paciente.mass,paciente.pedi,paciente.age]).reshape(-1,1).T
            new_prediction = logreg.predict(X_new)
            n=new_prediction[0]
            porcen=logreg.predict_proba(X_new)[0][1]*100
            paciente.porcentaje=porcen
            paciente.save()
            consulta=Paciente.objects.filter(cedula=paciente.cedula)
            nombre=paciente.Nombre
            return render(request,"resultado.html",{'cedula':paciente.cedula,'n':n,'porcentaje':porcen,'consulta':consulta,'nombre':nombre})



    else:
        form = PacienteForm()
    return render(request, 'paciente_edit.html', {'form': form})
def estadistica(request):
    from pacientes.models import PacienteDB


    # csv_filepathname = "C:/Users/kevin/PycharmProjects/Diabetes/pima-indians-diabetes.csv"
    # your_djangoproject_home = "C:/Users/kevin/PycharmProjects"
    #
    # import sys, os
    # sys.path.append(your_djangoproject_home)
    # os.environ['DJANGO_SETTINGS_MODULE'] = 'Diabetes.settings'
    #
    #
    # import csv
    # dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
    #
    # for row in dataReader:
    #     paciente = PacienteDB()
    #     print(paciente)
    #     paciente.preg = row[0]
    #     paciente.plas = row[1]
    #     paciente.press = row[2]
    #     paciente.skin = row[3]
    #     paciente.test = row[4]
    #     paciente.mass = row[5]
    #     paciente.pedi = row[6]
    #     paciente.age = row[7]
    #     paciente.clase = row[8]
    #     paciente.save()
    from django.db.models import Count
    pregR = PacienteDB.objects.values('preg').annotate(num=Count('preg'))
    plasR = PacienteDB.objects.values('plas').annotate(num=Count('plas'))
    pressR = PacienteDB.objects.values('press').annotate(num=Count('press'))
    skinR = PacienteDB.objects.values('skin').annotate(num=Count('skin'))
    testR = PacienteDB.objects.values('test').annotate(num=Count('test'))
    massR = PacienteDB.objects.values('mass').annotate(num=Count('mass'))
    pediR = PacienteDB.objects.values('pedi').annotate(num=Count('pedi'))
    ageR = PacienteDB.objects.values('age').annotate(num=Count('age'))
    claseR = PacienteDB.objects.values('clase').annotate(num=Count('clase'))
    return render(request, 'estadistica.html',{'pregR':pregR, 'plasR':plasR,'pressR':pressR,'skinR':skinR,'testR':testR,'massR':massR,'pediR':pediR,'ageR':ageR,'claseR':claseR})

#def grafica(request):