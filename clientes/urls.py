from django.urls import path

from .views import form_cliente, home, clientes_por_dia, historial

urlpatterns = [
path('', home, name='home'),
path('home/', home, name='home'),
    path('form/', form_cliente, name='form'),
    path('clientes/<str:dia>/', clientes_por_dia, name='clientes_por_dia'),
    path('historial/', historial, name='historial'),
]