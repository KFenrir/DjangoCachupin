from django.shortcuts import render
from .models import Cliente

# Create your views here.


def main(request):
    context={}
    return render(request, "pages/main.html", context)

def login(request):
    context = {}
    
    if request.method != "POST":
        return render(request, "pages/login.html", context)
    else:
        correo = request.POST["correo"]
        contraseña = request.POST["password"]
        if correo == "correo" and contraseña == "password":
            request.session["correo"] = correo
            usuarios = Cliente.objects.all()
            context = {"usuario": usuarios}
            return render(request, "pages/main.html", context)
        else:
            context = {"mensaje": "Usuario y/o Contraseña incorrecto"}
            return render(request, "pages/login.html", context)

def registro(request):
    if request.method != "POST":
        cliente = Cliente.objects.all()
        context = {"cliente" : cliente}
        return render(request, "pages/registro.html", context)
    else:
        nombre = request.POST["nombre"]
        apPaterno = request.POST["apPaterno"]
        apMaterno = request.POST["apMaterno"]
        correo = request.POST["correo"]
        contraseña = request.POST["password"]
        confirmar_contraseña = request.POST["password2"]
        region = request.POST["regiones"]
        
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
    return render(request, "pages/collar_gatos.html", context)

def carrito(request):
    context={}
    return render(request, "pages/carrito.html", context)

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