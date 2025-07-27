
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

class CustomAuthenticationForm(AuthenticationForm):
    error_messages = {
        'invalid_login': _(
            "Por favor, introduce un usuario y contraseña correctos. Ten en cuenta que ambos campos pueden ser sensibles a mayúsculas/minúsculas."
        ),
        'inactive': _("Esta cuenta está inactiva."),
    }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django.core.exceptions import ValidationError

class RegistroUsuarioForm(UserCreationForm):
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        # Solo requerir mínimo 4 caracteres
        if len(password1) < 4:
            raise ValidationError('La contraseña debe tener al menos 4 caracteres.')
        return password1

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
