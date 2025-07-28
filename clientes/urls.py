from django.urls import path


from .views import form_cliente, home, clientes_por_dia, historial, signup, login_view, logout_view

urlpatterns = [
    path('', signup, name='signup'),
    path('home/', home, name='home'),
    path('form/', form_cliente, name='form'),
    path('clientes/<str:dia>/', clientes_por_dia, name='clientes_por_dia'),
    path('historial/', historial, name='historial'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]