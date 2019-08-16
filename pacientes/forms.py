from django import forms

from .models import Paciente

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('cedula','Nombre','preg', 'plas','press','skin','test','mass','pedi','age')

