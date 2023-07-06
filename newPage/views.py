from django.shortcuts import render
from newPage.carrito import Carrito
from .models import Cliente, Productos
# Create your views here.


def main(request):
    context={}
    return render(request, "pages/main.html", context)

def login(request):
    context = {}
    
    if request.method != "POST":
        return render(request, "pages/login.html", context)
    else:
        username = request.POST["correo"]
        password = request.POST["contraseña"]

def registro(request):
    if request.method != "POST":
        cliente = Cliente.objects.all()
        context = {"cliente" : cliente}
        return render(request, "pages/registro.html", context)
    else:
        nombre = request.POST.get('correo')
        apPaterno = request.POST.get('apPaterno')
        apMaterno = request.POST.get('apMaterno')
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña')
        confirmar_contraseña = request.POST.get('contraseña2')
        region = request.POST.get('region')
        
    objCliente = Cliente.objects.create(
        correo = correo,
        nombre = nombre,
        apPaterno = apPaterno,
        apMaterno = apMaterno,
        region = region,
        contraseña = contraseña,
        confirmar_contraseña = confirmar_contraseña,
    )
    objCliente.save()
    print("Agregado con exito")
    print(objCliente)
    context = {"mensaje": "OK Registrado Correctamente"}
    return render(request, "pages/login.html", context) 

def gatos(request):
    context={}
    return render(request, "pages/gatos.html", context)

def perros(request):
    context={}
    return render(request, "pages/perros.html", context)

def arnes_gatos(request):
    context={}
    return render(request, "pages/arnes_gatos.html", context)

def bandana_gatos(request):
    context={}
    return render(request, "pages/bandana_gatos.html", context)

def collar_gatos(request):
    context={}
    return render(request, "pages/carrito.html", context)

def carrito(request):
    context={}
    return render(request, "pages/carrito.html", context)

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.agregar(producto)
    return render(request, "pages/carrito.html")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return render(request, "pages/carrito.html")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id=producto_id)
    carrito.restar(producto)
    return render(request, "pages/carrito.html")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, "pages/carrito.html")

def catalogo(request):
    context={}
    return render(request, "pages/catalogo.html", context)

def tallas(request):
    context={}
    return render(request, "pages/tallas.html", context)

def suscripciones(request):
    context={}
    return render(request, "pages/suscripciones.html", context)

def nosotros(request):
    context={}
    return render(request, "pages/nosotros.html", context)

def arnes_perros(request):
    context={}
    return render(request, "pages/arnes_perros.html", context)

def bandana_perros(request):
    context={}
    return render(request, "pages/bandana_perros.html", context)

def collar_perros(request):
    context={}
    return render(request, "pages/collar_perros.html", context)

def tienda(request):
    productos = Productos.objects.all()
    return render(request, "tienda.html", {'productos':Productos})