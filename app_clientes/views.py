from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Servicio
from django.urls import reverse


def inicio_taller(request):
    # página principal de la app (taller)
    return render(request, 'inicio.html', {})


def agregar_clientes(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        apellido = request.POST.get('apellido', '').strip()
        email = request.POST.get('email', '').strip() or None
        rfc = request.POST.get('rfc', '').strip() or None
        telefono = request.POST.get('telefono', '').strip() or None
        direccion = request.POST.get('direccion', '').strip() or None
        cliente = Cliente(
            nombre=nombre,
            apellido=apellido,
            email=email,
            rfc=rfc,
            telefono=telefono,
            direccion=direccion,
        )
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'clientes/agregar_clientes.html', {})

def ver_clientes(request):
    clientes = Cliente.objects.all().order_by('apellido', 'nombre')
    return render(request, 'clientes/ver_clientes.html', {'clientes': clientes})

def actualizar_clientes(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'clientes/actualizar_clientes.html', {'cliente': cliente})

def realizar_actualizacion_clientes(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre', cliente.nombre).strip()
        cliente.apellido = request.POST.get('apellido', cliente.apellido).strip()
        email = request.POST.get('email', '').strip()
        cliente.email = email or None
        rfc = request.POST.get('rfc', '').strip()
        cliente.rfc = rfc or None
        telefono = request.POST.get('telefono', '').strip()
        cliente.telefono = telefono or None
        direccion = request.POST.get('direccion', '').strip()
        cliente.direccion = direccion or None
        cliente.save()
        return redirect('ver_clientes')
    # si llama GET, redirigir a formulario de edición
    return redirect('actualizar_clientes', cliente_id=cliente.id)

def borrar_clientes(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'clientes/borrar_clientes.html', {'cliente': cliente})



def agregar_servicio(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST.get('descripcion', '') # Permite que sea opcional
        precio_base = request.POST['precio_base']
        # el modelo define el campo como tiempo_est (minutos)
        tiempo_est = request.POST.get('tiempo_est', '0')
        aplica_garantia = 'aplica_garantia' in request.POST # True si está marcado, False si no

        Servicio.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio_base=precio_base,
            tiempo_est=tiempo_est,
            aplica_garantia=aplica_garantia
        )
        return redirect('ver_servicio')
    return render(request, 'servicio/agregar_servicio.html')

def ver_servicio(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicio/ver_servicio.html', {'servicios': servicios})

def actualizar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    return render(request, 'servicio/actualizar_servicio.html', {'servicio': servicio})

def realizar_actualizacion_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    if request.method == 'POST':
        servicio.nombre = request.POST.get('nombre', servicio.nombre)
        servicio.descripcion = request.POST.get('descripcion', servicio.descripcion)
        servicio.precio_base = request.POST.get('precio_base', servicio.precio_base)
        servicio.tiempo_est = request.POST.get('tiempo_est', servicio.tiempo_est)
        servicio.aplica_garantia = 'aplica_garantia' in request.POST
        servicio.save()
        return redirect('ver_servicio')
    return redirect('ver_servicio')

def borrar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    if request.method == 'POST':
        servicio.delete()
        return redirect('ver_servicio')
    return render(request, 'servicio/borrar_servicio.html', {'servicio': servicio})