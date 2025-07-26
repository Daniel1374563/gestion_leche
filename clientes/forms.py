from django.contrib.auth.forms import AuthenticationForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

from .models import Clientes

class ClientesForm(forms.ModelForm):
    DIAS_SEMANA = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]

    fecha_de_entrega = forms.ChoiceField(choices=DIAS_SEMANA, label="Día de la semana para la entrega")

    class Meta:
        model = Clientes
        fields = ['nombre', 'direccion', 'cantidad_de_litros', 'numero_de_telefono', 'fecha_de_entrega', 'importe_a_pagar', 'done']
