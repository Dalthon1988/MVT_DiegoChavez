
from django.shortcuts import render
from django.http import HttpResponse
from Familiares.models import info_familiares
from django.template import loader
# Create your views here.


def lista_familiares(request):
    
    family = info_familiares.objects.all()
    
    lista_nombres = []
    lista_apellidos = []
    lista_nacimiento = []
    lista_direcciones = []
    lista_ciudades = []
    
    
    for dato in family:
        lista_nombres.append(dato.nombre)
        lista_apellidos.append(dato.apellido)
        lista_nacimiento.append(dato.nacimiento)
        lista_direcciones.append(dato.direccion)
        lista_ciudades.append(dato.ciudad)
        
        lista_nombre_apellido = zip(lista_nombres,lista_apellidos)
        lista_nombre_nacimiento_direccion_ciudad = zip(lista_nombres,lista_nacimiento,lista_direcciones,lista_ciudades)
        
        
        plantilla = loader.get_template("Familia.html")
    # Le doy forma al contexto con las listas creadas, dandoles una clave-valor
    datos = {
        "nombres_apellidos": lista_nombre_apellido,
        "nombre_nacimiento_direccion_ciudad": lista_nombre_nacimiento_direccion_ciudad,
    }
    # renderizo y devuelvo
    documento = plantilla.render(datos)
    return HttpResponse(documento)
        
        
    
    
    
    