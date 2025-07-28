from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomAuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, login, logout

@login_required(login_url='clientes:login')
def logout_view(request):
    logout(request)
    return redirect('clientes:login')
from .forms import RegistroUsuarioForm, ClientesForm
from .models import Clientes
from django.views.decorators.csrf import csrf_exempt

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:home')
    else:
        form = UserCreationForm()
    # Si el usuario ya está autenticado, redirige a home
    if request.user.is_authenticated:
        return redirect('clientes:home')
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('clientes:home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('clientes:home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

@login_required(login_url='clientes:login')
def historial(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente_id')
        accion = request.POST.get('accion')
        if cliente_id and accion == 'eliminar':
            cliente = Clientes.objects.get(id=cliente_id)
            cliente.delete()
    clientes = Clientes.objects.filter(done=True)
    total_importe = sum([c.importe_a_pagar for c in clientes])
    return render(request, 'historial.html', {'clientes': clientes, 'total_importe': total_importe})

@login_required(login_url='clientes:login')
def form_cliente(request):
    editar_id = request.GET.get('editar')
    cliente_obj = None
    if editar_id:
        cliente_obj = Clientes.objects.get(id=editar_id)

    if request.method == 'POST':
        editar_id = request.GET.get('editar')
        if editar_id:
            cliente_obj = Clientes.objects.get(id=editar_id)
            form = ClientesForm(request.POST, instance=cliente_obj)
        else:
            form = ClientesForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            return redirect('clientes:clientes_por_dia', dia=cliente.fecha_de_entrega)
    else:
        if cliente_obj:
            form = ClientesForm(instance=cliente_obj)
        else:
            form = ClientesForm()
    return render(request, 'form.html', {'form': form, 'editar': editar_id})

@login_required(login_url='clientes:login')
def home(request):
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    return render(request, 'home.html', {'dias': dias})

@login_required(login_url='clientes:login')
def clientes_por_dia(request, dia):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente_id')
        accion = request.POST.get('accion')
        if cliente_id:
            cliente = Clientes.objects.get(id=cliente_id)
            if accion == 'cambiar_estado':
                cliente.done = not cliente.done
                cliente.save()
            elif accion == 'eliminar':
                cliente.delete()
    # Solo mostrar los clientes pendientes (no entregados)
    clientes = Clientes.objects.filter(fecha_de_entrega=dia, done=False)
    return render(request, 'clientes_por_dia.html', {'dia': dia, 'clientes': clientes})
