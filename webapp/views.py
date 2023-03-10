from django.http import HttpResponse
from django.shortcuts import render

from personas.models import Personas


def bienvenido(request):
    no_personas = Personas.objects.count()
    personas = Personas.objects.all()
    return render(request, 'bienvenido.html', {'no':no_personas, 'personas': personas})

def detallePersona(request, id):
    persona = Personas.objects.get(pk=id)
