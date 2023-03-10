from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render

from personas.models import Personas
from personas.forms import PersonaForm

def detallePersona(request, id):
    #persona = Personas.objects.get(pk=id)
    persona = get_object_or_404(Personas, pk=id)
    return render(request, 'detalle.html', {'persona':persona})


def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm()
    return render(request, 'addPersona.html', {'formaPersona':formaPersona })
